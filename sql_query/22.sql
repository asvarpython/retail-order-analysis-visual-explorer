# 22.Which product has the highest total sales quantity?

SELECT product_id, SUM(quantity) AS total_quantity
FROM product_details
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 1;

