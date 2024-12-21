# 21.What is the total discount amount given for each product category?

SELECT category, SUM(discount) AS total_discount
FROM product_details
GROUP BY category;