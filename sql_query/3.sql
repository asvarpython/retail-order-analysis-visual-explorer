# 3. Calculate the total discount given for each category:
    
SELECT category, SUM(discount) AS total_discount
FROM product_details
GROUP BY category;
