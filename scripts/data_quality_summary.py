import pandas as pd
from pathlib import Path

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Raw data folder
RAW_DATA = BASE_DIR / "data" / "raw"

# CSV files list
csv_files = list(RAW_DATA.glob("*.csv"))

print("\n----- DATA QUALITY SUMMARY -----")

# Loop through each CSV file
for file in csv_files:

    print(f"\nChecking File: {file.name}")

    # Load CSV
    df = pd.read_csv(file)

    # Shape
    print("Shape:", df.shape)

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate rows
    print("\nDuplicate Rows:", df.duplicated().sum())

    # First 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

print("\nData Quality Check Completed Successfully.")