"""
Mutual Fund Analytics Capstone

Recommends top mutual funds based on
risk grade and Sharpe ratio.
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

scheme_perf = pd.read_csv(
    BASE_DIR / "data" / "processed" / "cleaned_scheme_performance.csv"
)

def recommend_funds(risk_appetite):

    filtered = scheme_perf[
        scheme_perf['risk_grade'].str.lower()
        == risk_appetite.lower()
    ]

    recommendations = (
        filtered
        .sort_values(
            by='sharpe_ratio',
            ascending=False
        )[
            ['scheme_name',
             'risk_grade',
             'sharpe_ratio']
        ]
        .head(3)
    )

    return recommendations

print("\nTop Moderate Risk Funds:\n")
print(recommend_funds('Moderate'))