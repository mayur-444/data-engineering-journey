SELECT customer_name, product_name
FROM customers

JOIN orders
ON customers.customer_id = orders.customer_id

JOIN order_items
ON orders.order_id = order_items.order_id

JOIN products
ON order_items.product_id = products.product_id;

SELECT customer_name, SUM(amount)
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customer_name;