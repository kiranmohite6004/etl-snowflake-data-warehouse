def transform_sales_data(df):
    df["revenue"] = df["quantity"] * df["price"]
    return df
