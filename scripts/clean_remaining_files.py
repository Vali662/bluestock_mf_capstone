import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

raw_folder = BASE_DIR / "data" / "raw"
processed_folder = BASE_DIR / "data" / "processed"

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    print(f"\nProcessing {file}")

    input_file = raw_folder / file

    df = pd.read_csv(input_file)

    # remove duplicate rows
    df = df.drop_duplicates()

    output_file = processed_folder / f"cleaned_{file}"

    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file.name}")

print("\nAll remaining files cleaned successfully.")