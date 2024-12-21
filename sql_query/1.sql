# 1. Find top 10 highest revenue generating products

SELECT product_id, SUM(sale_price * quantity) AS total_revenue
FROM product_details
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;