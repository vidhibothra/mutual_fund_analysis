import os
import csv
import requests

os.makedirs("data/raw", exist_ok=True)

SCHEMES = {
    "125497": "HDFC_Top_100_Direct",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

def fetch_and_save_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching data for {scheme_name} (Code: {scheme_code})...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        meta = data.get("meta", {})
        nav_list = data.get("data", [])
        
        filename = f"data/raw/{scheme_name}_raw.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "nav", "scheme_code", "scheme_name", "fund_house"])
            
            for entry in nav_list:
                writer.writerow([
                    entry.get("date"),
                    entry.get("nav"),
                    scheme_code,
                    meta.get("scheme_name"),
                    meta.get("fund_house")
                ])
        print(f"Successfully saved to {filename}")
    except Exception as e:
        print(f"Error fetching {scheme_code}: {e}")

if __name__ == "__main__":
    for code, name in SCHEMES.items():
        fetch_and_save_nav(code, name)