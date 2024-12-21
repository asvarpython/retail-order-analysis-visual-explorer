# 7. Identify the top 3 segments with the highest quantity of orders: (doubt)

SELECT segment, COUNT(*) AS total_orders
FROM order_details
GROUP BY segment
ORDER BY total_orders DESC
LIMIT 3;
