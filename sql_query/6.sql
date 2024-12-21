# 6. Find the total profit per category:
    
SELECT category, SUM(profit) AS total_profit
FROM product_details
GROUP BY category;

