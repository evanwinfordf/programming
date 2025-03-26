import matplotlib.pyplot as plt

def plot_charging_stations(top_locations):
    """Plots the top EV charging station locations."""
    if top_locations is None:
        print("Error: No locations to plot")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(top_locations["Location"], top_locations["Demand"], color="blue")
    plt.xlabel("Locations")
    plt.ylabel("Demand")
    plt.title("Recommended EV Charging Stations")
    plt.xticks(rotation=45)
    plt.show()
