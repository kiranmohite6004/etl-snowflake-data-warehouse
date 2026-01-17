-- Total revenue by region
SELECT
    c.region,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.region;

-- Monthly revenue trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(revenue) AS monthly_revenue
FROM fact_sales
GROUP BY month
ORDER BY month;

-- Top selling products
SELECT
    p.product_name,
    SUM(f.quantity) AS total_quantity
FROM fact_sales f
JOIN dim_product p
    ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;
