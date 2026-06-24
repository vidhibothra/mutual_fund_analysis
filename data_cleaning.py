import os
import pandas as pd
from sqlalchemy import create_engine

# Make sure the target processed folder exists
os.makedirs("data/processed", exist_ok=True)

print("--- Day 2: Data Cleaning Started ---")

# 1. Clean nav_history.csv
try:
    nav_df = pd.read_csv("data/raw/nav_history.csv")
    nav_df['date'] = pd.to_datetime(nav_df['date'])
    nav_df = nav_df.sort_values(by=['amfi_code', 'date'])
    
    # Forward-fill missing values for weekends/holidays
    nav_df['nav'] = nav_df.groupby('amfi_code')['nav'].ffill()
    nav_df = nav_df.drop_duplicates()
    nav_df = nav_df[nav_df['nav'] > 0]
    
    nav_df.to_csv("data/processed/nav_history_cleaned.csv", index=False)
    print("✅ nav_history.csv cleaned successfully.")
except Exception as e:
    print(f"⚠️ Could not process nav_history: {e} (Ensure file exists in data/raw)")

# 2. Save SQLite Database locally
engine = create_engine("sqlite:///bluestock_mf.db")

# Example loading cleaned dataframe to SQL
# nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
print("📌 Local SQLite Database bluestock_mf.db initialized.")