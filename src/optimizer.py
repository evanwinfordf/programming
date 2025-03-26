import numpy as np

def optimize_charging_stations(city_demand, power_grid):
    """
    A simple algorithm to decide where to place EV charging stations.
    (For now, it just selects the top demand areas.)
    """
    if city_demand is None or power_grid is None:
        print("Error: Missing data")
        return None

    # Assume 'Location' and 'Demand' columns exist
    sorted_demand = city_demand.sort_values(by="Demand", ascending=False)
    
    # Select top 5 locations with the highest demand
    top_locations = sorted_demand.head(5)
    
    print("Recommended Charging Locations:")
    print(top_locations)

    return top_locations
