import pandas as pd

def load_data(file_path):
    """Loads a CSV file into a pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}, shape: {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None
