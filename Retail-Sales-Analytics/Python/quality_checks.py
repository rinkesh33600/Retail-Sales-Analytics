# Basic data quality checks

def check_nulls(df):
    """
    Checks and prints number of null values in each column
    """
    null_counts = df.isnull().sum()
    print("Null values per column:")
    print(null_counts)

def check_duplicates(df, column_name):
    """
    Checks and prints number of duplicate values in a column
    """
    duplicate_count = df[column_name].duplicated().sum()
    print(f"Duplicate values in {column_name}: {duplicate_count}")
    
def check_negative_values(df, column_name):
    """
    Checks if a column has negative values
    """
    negative_count = (df[column_name] < 0).sum()
    print(f"Negative values in {column_name}: {negative_count}")
