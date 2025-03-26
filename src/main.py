import numpy as np
from data_loader import load_data
from optimizer import optimize_charging_stations
from visualization import plot_charging_stations

def main():
    # Load data
    city_demand = load_data("data/city_demand.csv")
    power_grid = load_data("data/power_grid.csv")

    # Optimize charging station locations
    top_locations = optimize_charging_stations(city_demand, power_grid)

    # Visualize results
    plot_charging_stations(top_locations)

if __name__ == "__main__":
    main()
