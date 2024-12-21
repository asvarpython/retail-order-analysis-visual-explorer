# 16.Which product subcategory has the lowest average discount percentage?

SELECT sub_category, AVG(discount_percent) AS avg_discount_percent
FROM product_details
GROUP BY sub_category
ORDER BY avg_discount_percent ASC
LIMIT 1;