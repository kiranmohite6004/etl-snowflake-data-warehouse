from snowflake.connection import get_snowflake_connection

def load_fact_sales(df):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO fact_sales 
            (order_id, order_date, customer_id, product_id, quantity, revenue)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                row["order_id"],
                row["order_date"],
                row["customer_id"],
                1,
                row["quantity"],
                row["revenue"]
            )
        )

    cursor.close()
    conn.close()
