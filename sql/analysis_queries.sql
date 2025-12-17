-- Churn rate by contract type
SELECT contract,
       COUNT(*) AS customers,
       ROUND(AVG(churn_value) * 100, 2) AS churn_rate_percent
FROM telco
GROUP BY contract
ORDER BY churn_rate_percent DESC;

-- Churn by tenure group
SELECT tenure_group,
       COUNT(*) AS customers,
       ROUND(AVG(churn_value) * 100, 2) AS churn_rate_percent
FROM telco
GROUP BY tenure_group;

-- Churn by internet service
SELECT internet_service,
       COUNT(*) AS customers,
       ROUND(AVG(churn_value) * 100, 2) AS churn_rate_percent
FROM telco
GROUP BY internet_service;

-- Top churn reasons
SELECT churn_reason,
       COUNT(*) AS churn_count
FROM telco
WHERE churn_value = 1
GROUP BY churn_reason
ORDER BY churn_count DESC
LIMIT 10;
