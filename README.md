# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project was developed as part of the Bluestock Data Analyst Internship Program.

The objective is to analyze mutual fund industry data, evaluate fund performance, study investor behavior, and build an interactive analytics dashboard using Python, SQLite, and Power BI.

---

## Objectives

* Build an ETL pipeline for mutual fund datasets
* Clean and validate financial data
* Perform exploratory data analysis (EDA)
* Calculate performance metrics (Alpha, Beta, Sharpe Ratio, Sortino Ratio)
* Conduct advanced analytics (VaR, CVaR, Rolling Sharpe)
* Analyze investor behavior and SIP continuity
* Build an interactive Power BI dashboard
* Generate investment insights and recommendations

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
└── README.md
```

## Dataset Description

| Dataset               | Description                  |
| --------------------- | ---------------------------- |
| Fund Master           | Scheme information           |
| NAV History           | Historical NAV values        |
| AUM by Fund House     | Assets under management      |
| Monthly SIP Inflows   | SIP investment trends        |
| Category Inflows      | Category-wise fund flows     |
| Industry Folio Count  | Investor folio statistics    |
| Scheme Performance    | Returns and risk metrics     |
| Investor Transactions | Investor activity records    |
| Portfolio Holdings    | Fund holdings and sectors    |
| Benchmark Indices     | Market benchmark performance |

---

## How to Run ETL

```bash
python scripts/data_ingestion.py
python scripts/clean_nav_history.py
python scripts/load_to_sqlite.py
```

Or run:

```bash
python scripts/run_pipeline.py
```

---

## How to Open Dashboard

1. Open Power BI Desktop
2. Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

3. Refresh data if required.

---

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard (.pbix)
* EDA Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Recommender Script

---

## Author

Vali Shaik

Bluestock Data Analyst Internship
2026
