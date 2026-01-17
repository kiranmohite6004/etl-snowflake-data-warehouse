def run_data_quality_checks(df):
    assert df["order_id"].isnull().sum() == 0, "Null order_id found"
    assert (df["quantity"] > 0).all(), "Invalid quantity found"
    assert (df["revenue"] > 0).all(), "Invalid revenue found"
