# Data Dictionary — Bluestock Mutual Fund Capstone

## 1. fact_nav

| Column Name | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| amfi_code   | INTEGER   | Unique AMFI scheme code   |
| date        | DATE      | NAV recorded date         |
| nav         | REAL      | Net Asset Value of scheme |

---

## 2. fact_performance

| Column Name       | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | INTEGER   | Unique scheme identifier      |
| scheme_name       | TEXT      | Name of mutual fund scheme    |
| fund_house        | TEXT      | AMC / fund house name         |
| category          | TEXT      | Fund category                 |
| return_1yr_pct    | REAL      | 1-year return percentage      |
| return_3yr_pct    | REAL      | 3-year return percentage      |
| return_5yr_pct    | REAL      | 5-year return percentage      |
| sharpe_ratio      | REAL      | Risk-adjusted return metric   |
| expense_ratio_pct | REAL      | Fund expense ratio percentage |
| risk_grade        | TEXT      | Risk classification           |

---

## 3. fact_transactions

| Column Name      | Data Type | Description                      |
| ---------------- | --------- | -------------------------------- |
| investor_id      | TEXT      | Unique investor ID               |
| transaction_date | DATE      | Transaction date                 |
| amfi_code        | INTEGER   | Mutual fund scheme code          |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption       |
| amount_inr       | REAL      | Transaction amount in INR        |
| state            | TEXT      | Investor state                   |
| city             | TEXT      | Investor city                    |
| payment_mode     | TEXT      | UPI / NetBanking / Cheque etc    |
| kyc_status       | TEXT      | Investor KYC verification status |

---

## Source References

* Mutual Fund NAV API: mfapi.in
* Internship datasets provided by Bluestock Fintech
* AMFI Mutual Fund classification data
