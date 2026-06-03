import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
input_file = BASE_DIR / "data" / "raw" / "02_nav_history.csv"
output_file = BASE_DIR / "data" / "processed" / "cleaned_nav_history.csv"

# Load dataset
df = pd.read_csv(input_file)

print("\nOriginal Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort values
df = df.sort_values(by=["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill missing NAV values
df["nav"] = df["nav"].ffill()

# Keep only NAV > 0
df = df[df["nav"] > 0]

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Final shape
print("\nCleaned Shape:", df.shape)

# Save cleaned CSV
df.to_csv(output_file, index=False)

print("\nCleaned nav_history.csv saved successfully.")