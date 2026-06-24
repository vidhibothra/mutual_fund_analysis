import os
import glob
import pandas as pd

def load_and_inspect_datasets():
    print("--- Loading and Inspecting CSV Datasets ---")
    csv_files = glob.glob("data/raw/*.csv")
    
    if not csv_files:
        print("No CSV files found in data/raw/. Please run live_nav_fetch.py first.")
        return
        
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        print(f"\n{'='*40}\nDataset: {file_name}\n{'='*40}")
        try:
            df = pd.read_csv(file_path)
            print(f"Shape: {df.shape}")
            print("\nData Types:")
            print(df.dtypes)
            print("\nFirst 3 Rows:")
            print(df.head(3))
        except Exception as e:
            print(f"Error loading {file_name}: {e}")

if __name__ == "__main__":
    load_and_inspect_datasets()