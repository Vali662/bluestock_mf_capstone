import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
input_file = BASE_DIR / "data" / "raw" / "08_investor_transactions.csv"

output_file = BASE_DIR / "data" / "processed" / "cleaned_investor_transactions.csv"

# Load dataset
df = pd.read_csv(input_file)

print("\nOriginal Shape:", df.shape)

# Print columns
print("\nColumns:")
print(df.columns)

# Convert date column
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# Keep valid transaction types
valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]

df = df[df["transaction_type"].isin(valid_types)]

# Keep amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.upper()
)

# Keep valid KYC values
valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Final shape
print("\nCleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned investor_transactions.csv saved successfully.")