# EV Charging Station Optimizer

## 🚀 Title
**EV Charging Station Optimizer**

## 📖 Description
A Python-based command-line application that assists urban planners and businesses in finding optimal locations for EV charging stations. It was developed to support sustainable city planning, reduce charging congestion, and improve accessibility using data-driven methods.

## 📊 Architecture Diagram
Input CSVs (EV Demand + Grid Capacity)
↓
Geocoder → Demand Weighting → KMeans Clustering
↓                           ↓
Optimal Coordinates       ↘
↓                        ↓
Summary CSV        Map (HTML)     Transaction Log (JSON)

## 🛠 How to Run
1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate

Install requirements:
pip install -r requirements.txt

Run the app:
python ev_optimizer.py --input data/city_demand.csv --capacity data/power_grid.csv --stations 3

🧠 Challenges

Geocoding non-Canadian place names was inaccurate by default

Balancing cluster optimization with demand weighting

Ensuring CLI usability and readable outputs

🚀 Future Enhancements

Add GUI using Tkinter or PyQt

Include multi-city analysis with shapefile input

Optimize based on live traffic and power load data

Deploy as a packaged binary for planners


📁 Output

reports/summary_<date>.csv

reports/map_<date>.html

logs/transaction_log.json

🧰 Tech Stack

Python

pandas, NumPy

sci-kit-learn

folium, goopy

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


🌍 License
MIT
---
