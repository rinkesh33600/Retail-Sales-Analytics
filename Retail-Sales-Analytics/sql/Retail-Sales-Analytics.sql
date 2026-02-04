CREATE DATABASE analytics_platform;
USE analytics_platform;
CREATE TABLE staging_customers (
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50)
);
SELECT * FROM staging_customers;
CREATE TABLE staging_orders (
    order_id VARCHAR(20),
    order_date DATE,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    store_id VARCHAR(20),
    promo_id VARCHAR(20),
    quantity INT,
    sales_amount DECIMAL(10,2),
    cost_amount DECIMAL(10,2)
);
SELECT COUNT(*) FROM staging_orders;
CREATE TABLE staging_products (
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    brand VARCHAR(50),
    sub_category VARCHAR(50),
    category VARCHAR(50)
);
SELECT * FROM staging_products;
CREATE TABLE IF NOT EXISTS staging_stores (
    store_id VARCHAR(20),
    store_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    region VARCHAR(50),
    store_type VARCHAR(50)
);
SELECT order_id, order_date FROM staging_orders LIMIT 5;
SELECT * FROM staging_stores;
CREATE TABLE staging_promotions (
    promo_id VARCHAR(20),
    promotion_type VARCHAR(100),
    discount_pct INT,
    start_date DATE,
    end_date DATE
);
SELECT * FROM staging_promotions;
CREATE TABLE dim_customers AS
SELECT DISTINCT
    customer_id,
    customer_name,
    gender,
    age,
    city,
    state,
    country
FROM staging_customers;
CREATE TABLE dim_stores AS
SELECT DISTINCT
    store_id,
    store_name,
    city,
    state,
    region,
    store_type
FROM staging_stores;
CREATE TABLE dim_promotions AS
SELECT DISTINCT
    promo_id,
    promotion_type,
    discount_pct,
    start_date,
    end_date
FROM staging_promotions;
SHOW TABLES;
CREATE TABLE dim_products AS
SELECT DISTINCT
    product_id,
    product_name,
    brand,
    sub_category,
    category
FROM staging_products;
CREATE TABLE fact_sales AS
SELECT
    o.order_id,
    o.order_date,
    o.customer_id,
    o.product_id,
    o.store_id,
    o.promo_id,
    o.quantity,
    o.sales_amount,
    o.cost_amount,
    (o.sales_amount - o.cost_amount) AS profit
FROM staging_orders o;
select * from fact_sales LIMIT 5;
