# 13.What is the total quantity of products sold in each region?

SELECT region, SUM(quantity) AS total_quantity
FROM order_details
JOIN product_details ON order_details.order_id = product_details.order_id
GROUP BY region;



