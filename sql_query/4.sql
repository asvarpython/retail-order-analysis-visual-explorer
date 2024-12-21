# 4. Find the average sale price per product category:
   
SELECT category, AVG(sale_price) AS avg_sale_price
FROM product_details
GROUP BY category;