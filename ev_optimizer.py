import argparse
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import json
import os
from datetime import datetime
from geopy.geocoders import Nominatim
import folium

# Create necessary folders if they don't exist
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

def geocode_locations(ev_data):
    geolocator = Nominatim(user_agent="ev_optimizer")
    latitudes = []
    longitudes = []
    
    for location in ev_data["Location"]:
        try:
            geo = geolocator.geocode(f"{location}, Ontario, Canada", addressdetails=True)
            if geo:
                latitudes.append(geo.latitude)
                longitudes.append(geo.longitude)
            else:
                latitudes.append(None)
                longitudes.append(None)
        except:
            latitudes.append(None)
            longitudes.append(None)

    ev_data["latitude"] = latitudes
    ev_data["longitude"] = longitudes
    ev_data.dropna(subset=["latitude", "longitude"], inplace=True)
    return ev_data

def load_data(ev_data_path, grid_data_path):
    ev_data = pd.read_csv(ev_data_path)
    grid_data = pd.read_csv(grid_data_path)
    if "latitude" not in ev_data.columns or "longitude" not in ev_data.columns:
        ev_data = geocode_locations(ev_data)
    return ev_data, grid_data

def optimize_locations(ev_data, num_stations):
    coords = ev_data[["latitude", "longitude"]].values
    weights = ev_data["Demand"].values
    kmeans = KMeans(n_clusters=num_stations, random_state=42)
    kmeans.fit(coords, sample_weight=weights)
    centroids = kmeans.cluster_centers_
    ev_data["cluster"] = kmeans.labels_
    return centroids, ev_data

def save_transaction_log(input_path, capacity_path, centroids):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input_file": input_path,
        "capacity_file": capacity_path,
        "recommended_locations": centroids.tolist()
    }
    log_file = "logs/transaction_log.json"
    if os.path.exists(log_file):
        with open(log_file, "r+") as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    else:
        with open(log_file, "w") as file:
            json.dump([log_entry], file, indent=4)

def save_summary(centroids, ev_data):
    summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "num_clusters": len(centroids),
        "total_demand_points": len(ev_data),
        "centroid_coordinates": centroids.tolist()
    }
    summary_file = f"reports/summary_{datetime.now().strftime('%Y-%m-%d')}.csv"
    pd.DataFrame([summary]).to_csv(summary_file, index=False)
    print("\n✅ Summary saved at:", summary_file)

def plot_map(ev_data, centroids):
    m = folium.Map(location=[ev_data["latitude"].mean(), ev_data["longitude"].mean()], zoom_start=12)
    
    for _, row in ev_data.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            popup=f"{row['Location']} - Demand: {row['Demand']}",
            color="blue",
            fill=True
        ).add_to(m)

    for i, (lat, lon) in enumerate(centroids):
        folium.Marker(
            location=[lat, lon],
            popup=f"Station {i+1}",
            icon=folium.Icon(color="red")
        ).add_to(m)

    map_file = f"reports/map_{datetime.now().strftime('%Y-%m-%d')}.html"
    m.save(map_file)
    print("\n🗺️ Map saved at:", map_file)

def main():
    parser = argparse.ArgumentParser(description="EV Charging Station Optimizer")
    parser.add_argument("--input", type=str, required=True, help="Path to EV data CSV")
    parser.add_argument("--capacity", type=str, required=True, help="Path to grid capacity CSV")
    parser.add_argument("--stations", type=int, default=5, help="Number of stations to recommend")
    args = parser.parse_args()

    print("\n🔄 Loading data...")
    ev_data, grid_data = load_data(args.input, args.capacity)

    print("\n📍 Optimizing locations...")
    centroids, labeled_data = optimize_locations(ev_data, args.stations)

    print("\n📊 Recommended Charging Station Coordinates:")
    for i, (lat, lon) in enumerate(centroids):
        print(f"  {i+1}: Latitude: {lat:.4f}, Longitude: {lon:.4f}")

    save_transaction_log(args.input, args.capacity, centroids)
    save_summary(centroids, ev_data)
    plot_map(ev_data, centroids)

if __name__ == "__main__":
    main()
