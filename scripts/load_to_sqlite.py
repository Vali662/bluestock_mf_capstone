import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database path
db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"

# Create SQLite engine
engine = create_engine(f"sqlite:///{db_path}")

# Processed data folder
processed_path = BASE_DIR / "data" / "processed"

# Load cleaned datasets
nav_df = pd.read_csv(processed_path / "cleaned_nav_history.csv")

performance_df = pd.read_csv(
    processed_path / "cleaned_scheme_performance.csv"
)

transactions_df = pd.read_csv(
    processed_path / "cleaned_investor_transactions.csv"
)

# Save to SQLite tables
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("\nSQLite database created successfully.")

print("\nTables loaded:")
print("- fact_nav")
print("- fact_performance")
print("- fact_transactions")