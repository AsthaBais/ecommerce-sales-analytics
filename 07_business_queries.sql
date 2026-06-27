SELECT
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
SELECT
    c.customer_id,
    CONCAT(c.first_name,' ',c.last_name) AS customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_id, customer_name
ORDER BY total_spent DESC
LIMIT 10;
SELECT
    cat.category_name,
    SUM(oi.quantity) AS total_items_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
JOIN categories cat
ON p.category_id = cat.category_id
GROUP BY cat.category_name
ORDER BY total_items_sold DESC;
SELECT
    p.product_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;
SELECT
    c.customer_id,
    CONCAT(c.first_name,' ',c.last_name) AS customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, customer_name
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;
SELECT
    payment_method,
    COUNT(*) AS total_transactions
FROM payments
GROUP BY payment_method
ORDER BY total_transactions DESC;
SELECT
    ROUND(
        COUNT(DISTINCT r.order_id) * 100.0 /
        COUNT(DISTINCT o.order_id),
        2
    ) AS return_percentage
FROM orders o
LEFT JOIN returns r
ON o.order_id = r.order_id;
SELECT
    c.city,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.city
ORDER BY revenue DESC
LIMIT 10;
SELECT
    product_name,
    stock
FROM products
WHERE stock < 50
ORDER BY stock;
SELECT
    c.customer_id,
    CONCAT(c.first_name,' ',c.last_name) AS customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS lifetime_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_id, customer_name
ORDER BY lifetime_value DESC
LIMIT 20;