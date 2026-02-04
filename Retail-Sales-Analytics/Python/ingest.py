import pandas as pd
from config import RAW_DATA_PATH, CUSTOMERS_FILE, ORDERS_FILE , PRODUCTS_FILE , PROMOTIONS_FILE, STORES_FILE


def read_customers():
    """
    Reads customers CSV file and returns a DataFrame
    """
    file_path = RAW_DATA_PATH + "/" + CUSTOMERS_FILE
    df = pd.read_csv(file_path)
    return df

def read_orders():
    """
    Reads orders CSV file and returns a DataFrame
    """
    file_path = RAW_DATA_PATH + "/" + ORDERS_FILE
    df = pd.read_csv(file_path)
    return df

def read_products():
    """
    Reads products CSV file and returns a DataFrame
    """
    file_path = RAW_DATA_PATH + "/" + PRODUCTS_FILE
    df = pd.read_csv(file_path)
    return df

def read_promotions():
    """
    Reads orders CSV file and returns a DataFrame
    """
    file_path = RAW_DATA_PATH + "/" + PROMOTIONS_FILE
    df = pd.read_csv(file_path)
    return df

def read_stores():
    """
    Reads products CSV file and returns a DataFrame
    """
    file_path = RAW_DATA_PATH + "/" + STORES_FILE
    df = pd.read_csv(file_path)
    return df