"""
Mutual Fund Analytics Capstone

Fetches NAV data for mutual funds.
"""
import requests
import pandas as pd
from pathlib import Path

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data folder
RAW_DATA = BASE_DIR / "data" / "raw"

# Mutual fund schemes
funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

# Loop through all funds
for fund_name, scheme_code in funds.items():

    print(f"\nFetching data for {fund_name}...")

    # API URL
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    # Fetch data
    response = requests.get(url)

    # Convert JSON response
    data = response.json()

    # Fund scheme name
    print("Scheme Name:", data["meta"]["scheme_name"])

    # Convert NAV history to DataFrame
    df = pd.DataFrame(data["data"])

    # Output CSV path
    output_path = RAW_DATA / f"{fund_name}.csv"

    # Save CSV
    df.to_csv(output_path, index=False)

    print("Saved:", output_path)

print("\nAll mutual fund NAV data fetched successfully.")