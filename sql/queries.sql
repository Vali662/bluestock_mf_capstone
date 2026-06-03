-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by AMFI code
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total transaction amount by state
SELECT state, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 4. Count of transactions by type
SELECT transaction_type, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 5. Funds with expense ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1-year return
SELECT AVG(return_1yr_pct) AS avg_1yr_return
FROM fact_performance;

-- 7. Top 10 investors by investment amount
SELECT investor_id, SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;

-- 8. Number of investors by city tier
SELECT city_tier, COUNT(DISTINCT investor_id) AS investors
FROM fact_transactions
GROUP BY city_tier;

-- 9. Highest Sharpe ratio funds
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 10. Transactions with VERIFIED KYC
SELECT COUNT(*) AS verified_transactions
FROM fact_transactions
WHERE kyc_status = 'VERIFIED';