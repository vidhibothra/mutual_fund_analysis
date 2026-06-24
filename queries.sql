-- 1. Top funds by final recorded NAV
SELECT scheme_code, MAX(nav) as peak_nav 
FROM fact_nav 
GROUP BY scheme_code 
ORDER BY peak_nav DESC;

-- 2. Average NAV grouped by month
SELECT strftime('%Y-%m', date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. Total entries tracked per fund scheme
SELECT scheme_code, COUNT(*) as total_records 
FROM fact_nav 
GROUP BY scheme_code;