# transform.py
# Data transformation functions
import pandas as pd
def standardize_column_names(df):
    """
    Converts all column names to lowercase
    """
    df.columns = df.columns.str.lower()
    return df

def convert_order_date(df):
    """
    Converts order_date from DD-MM-YYYY to YYYY-MM-DD
    """
    df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y")
    return df

def convert_promo_dates(df):
    """
    Converts promo dates to MySQL-compatible strings (YYYY-MM-DD)
    Handles NaN safely
    """
    df["start_date"] = pd.to_datetime(df["start_date"], format="%d-%m-%Y", errors="coerce")
    df["end_date"] = pd.to_datetime(df["end_date"], format="%d-%m-%Y", errors="coerce")

    # Convert to string format MySQL understands
    df["start_date"] = df["start_date"].dt.strftime("%Y-%m-%d")
    df["end_date"] = df["end_date"].dt.strftime("%Y-%m-%d")

    # Replace NaN with None (MySQL NULL)
    df["start_date"] = df["start_date"].where(df["start_date"].notna(), None)
    df["end_date"] = df["end_date"].where(df["end_date"].notna(), None)

    return df
