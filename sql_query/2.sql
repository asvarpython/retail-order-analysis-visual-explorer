# 2. Find the top 5 cities with the highest profit margins (dout reg formula)

SELECT city, AVG(profit / sale_price) AS avg_profit_margin
FROM order_details
JOIN product_details ON order_details.order_id = product_details.order_id
GROUP BY city
ORDER BY avg_profit_margin DESC
LIMIT 5;
