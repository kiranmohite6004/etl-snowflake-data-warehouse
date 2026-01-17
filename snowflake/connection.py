import snowflake.connector

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        account="YOUR_ACCOUNT",
        warehouse="ETL_WH",
        database="SALES_DB",
        schema="ANALYTICS"
    )
    return conn
