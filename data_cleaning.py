import os
import glob
import pandas as pd
from sqlalchemy import create_engine

# Make sure folders exist
os.makedirs("data/processed", exist_ok=True)

print("--- Day 2: Data Cleaning Started ---")

# Setup local SQLite Database
engine = create_engine("sqlite:///bluestock_mf.db")

# Find all raw CSV files fetched on Day 1
raw_files = glob.glob("data/raw/*_raw.csv")

if not raw_files:
    print("⚠️ No raw CSV files found in data/raw/. Did you run live_nav_fetch.py first?")
else:
    for file_path in raw_files:
        file_name = os.path.basename(file_path)
        try:
            # Load data
            df = pd.read_csv(file_path)
            
            # 1. Parse dates to datetime and sort
            df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
            df = df.sort_values(by=['scheme_code', 'date'])
            
            # 2. Forward-fill missing NAV values for holidays/weekends
            df['nav'] = df.groupby('scheme_code')['nav'].ffill()
            
            # 3. Remove duplicates and validate NAV > 0
            df = df.drop_duplicates()
            df = df[df['nav'] > 0]
            
            # Define output name
            clean_file_name = file_name.replace("_raw.csv", "_cleaned.csv")
            output_path = f"data/processed/{clean_file_name}"
            
            # Save cleaned CSV
            df.to_csv(output_path, index=False)
            print(f"✅ Cleaned and saved: {clean_file_name}")
            
            # Load into SQLite database table
            table_name = "fact_nav"
            df.to_sql(table_name, engine, if_exists="append", index=False)
            
        except Exception as e:
            print(f"⚠️ Error processing {file_name}: {e}")

print("\n📌 Local SQLite Database bluestock_mf.db updated successfully.")