# 12.Which product category has the highest average profit margin?

SELECT category, AVG(profit / sale_price) * 100 AS avg_profit_margin
FROM product_details
GROUP BY category
ORDER BY avg_profit_margin DESC
LIMIT 1;