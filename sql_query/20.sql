# 20.What is the total number of unique products sold in each category?
    
SELECT category, COUNT(DISTINCT product_id) AS unique_products
FROM product_details
GROUP BY category;


