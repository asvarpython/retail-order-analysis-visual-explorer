# 14.Which city has the highest average order value? (doubt)

SELECT 
    city, 
    AVG(sale_price * quantity) AS avg_order_value
FROM product_details
JOIN order_details ON product_details.order_id = order_details.order_id
GROUP BY city
ORDER BY avg_order_value DESC
LIMIT 1;

