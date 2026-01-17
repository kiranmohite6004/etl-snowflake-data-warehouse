CREATE OR REPLACE TABLE dim_customer (
    customer_id INT,
    region STRING
);

CREATE OR REPLACE TABLE dim_product (
    product_id INT AUTOINCREMENT,
    product_name STRING
);

CREATE OR REPLACE TABLE fact_sales (
    order_id INT,
    order_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    revenue NUMBER(10,2)
);
