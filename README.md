# EV Charging Station Optimizer

## 🔍 Overview
A Python-based command-line application that analyzes EV demand and grid data to recommend optimal locations for EV charging stations. It uses clustering algorithms, geocoding, and visualization to ensure accessibility, efficiency, and transparency.

## 🚀 Features
- Demand-weighted KMeans clustering
- Location geocoding
- Interactive map output
- Transaction logging (JSON)
- Summary reporting (CSV)

## 📂 Folder Structure
project/
├── data/                  # Input data (CSV files)
├── logs/                  # JSON transaction logs
├── reports/               # Summary reports and HTML maps
├── venv/                  # Virtual environment (if used)
├── ev_optimizer.py        # Main application script

## 📅 Usage
```bash
# Activate your environment
source venv/bin/activate

# Run the optimizer
python ev_optimizer.py --input data/city_demand.csv --capacity data/power_grid.csv --stations 3

📊 Output

reports/summary_<date>.csv ✔️

reports/map_<date>.html 🔻

logs/transaction_log.json 🔐

📄 Requirements

Python 3.8+

pandas, numpy, scikit-learn, folium, geopy

Install with:
pip install -r requirements.txt

🌍 License
MIT
---