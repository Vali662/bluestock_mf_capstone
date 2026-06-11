"""
Mutual Fund Analytics Capstone

Reads raw mutual fund datasets
for processing and analysis.
"""
import pandas as pd
from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data folder
RAW_DATA = BASE_DIR / "data" / "raw"

# Get all CSV files
csv_files = list(RAW_DATA.glob("*.csv"))

print("\n===== DATA INGESTION STARTED =====")

# Loop through all CSV files
for file in csv_files:

    print(f"\nLoading File: {file.name}")

    try:
        # Read CSV file
        df = pd.read_csv(file)

        # Print shape
        print("Shape:", df.shape)

        # Print datatypes
        print("\nData Types:")
        print(df.dtypes)

        # Print first 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Print missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error reading file:", e)

print("\n===== ALL DATASETS LOADED SUCCESSFULLY =====")