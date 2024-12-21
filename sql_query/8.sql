# 8. Determine the average discount percentage given per region:

SELECT region, AVG(discount_percent) AS avg_discount_percent
FROM order_details
JOIN product_details ON order_details.order_id = product_details.order_id
GROUP BY region;