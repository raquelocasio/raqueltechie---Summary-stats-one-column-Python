import pandas as pd

def calculate_summary_statistics(dataframe, column_name):

    # Check if the column exists in the DataFrame
    if column_name not in dataframe.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    # Select the specified column
    column = dataframe[column_name]

    # Calculate summary statistics
    summary_stats = column.describe()

    return summary_stats