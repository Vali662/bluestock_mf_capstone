import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
input_file = BASE_DIR / "data" / "raw" / "07_scheme_performance.csv"

output_file = BASE_DIR / "data" / "processed" / "cleaned_scheme_performance.csv"

# Load dataset
df = pd.read_csv(input_file)

print("\nOriginal Shape:", df.shape)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert expense ratio column to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Keep valid expense ratio values
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
df = df.drop_duplicates()

# Missing values summary
print("\nMissing Values:")
print(df.isnull().sum())

# Final shape
print("\nCleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned scheme_performance.csv saved successfully.")