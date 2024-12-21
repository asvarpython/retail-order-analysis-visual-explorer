# 10. Calculate the total revenue generated per year:

SELECT YEAR(order_date) AS year, SUM(sale_price * quantity) AS total_revenue
FROM order_details
JOIN product_details ON order_details.order_id = product_details.order_id
GROUP BY year;