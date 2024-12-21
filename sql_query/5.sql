# 5. Find the region with the highest average sale price:

SELECT region, AVG(sale_price) AS avg_sale_price
FROM order_details
JOIN product_details ON order_details.order_id = product_details.order_id
GROUP BY region
ORDER BY avg_sale_price DESC
LIMIT 1;

