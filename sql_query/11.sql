# 11.Which customer segment has the highest average order value? (doubt)

SELECT segment, AVG(sale_price * quantity) AS avg_order_value
FROM product_details
JOIN order_details ON product_details.order_id = order_details.order_id
GROUP BY segment
ORDER BY avg_order_value DESC
LIMIT 1;
