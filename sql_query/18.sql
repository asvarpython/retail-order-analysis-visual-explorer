# 18.Which product category has the highest average quantity per order?

SELECT category, AVG(quantity) AS avg_quantity
FROM product_details
GROUP BY category
ORDER BY avg_quantity DESC
LIMIT 1;


