# 17.What is the total number of orders placed in each year?

SELECT YEAR(order_date) AS year, COUNT(*) AS total_orders
FROM order_details
GROUP BY year;