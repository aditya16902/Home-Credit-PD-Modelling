import pandas as pd


def check_null(df):
    null_count = df.isnull().sum() / len(df) * 100
    return pd.DataFrame(
        null_count[null_count > 0].sort_values(ascending=False), columns=["percentage"]
    )
