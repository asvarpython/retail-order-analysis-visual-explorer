# 9. Find the product category with the highest total profit:

SELECT category, SUM(profit) AS total_profit
FROM product_details
GROUP BY category
ORDER BY total_profit DESC
LIMIT 1;



