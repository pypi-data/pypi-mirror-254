import pandas as pd
import numpy as np


def cor_eda(dataset, na_handling="drop"):
    """
    Perform exploratory data analysis (EDA) by calculating the correlation between numerical variables.
    This function isolates the numerically variables from the given dataset and handles NA values,
    calculates the correlation between each pair of variables, and displays the results in a table format.

    Parameters:
    dataset (DataFrame): The DataFrame should include various types of variables
    na_handling (str, optional): Specifies the method to handle missing values (NAs). Options are 'drop', 'mean', 'median', and 'value'. Default is 'drop'.
        - 'drop': Drops rows with any NAs.
        - 'mean': Replaces NAs with the mean value of the column.
        - 'median': Replaces NAs with the median value of the column.
        - 'value': Replaces NAs with a selected value.

    Returns:
    DataFrame: A DataFrame containing the correlation values between each pair of numerical variables.

    Example:
    cor_eda(data, na_handling='mean')
            age    salary
    age     1.0000   0.9769
    salary  0.9769   1.0000

    """
    # Isolate the numerical variables
    numerical_data = dataset.select_dtypes(include=["number"])

    if numerical_data.empty or numerical_data.shape[1] == 0:
        return "There are no numerical columns"

    # Handle missing values according to the specified method
    if na_handling == "drop":
        numerical_data = numerical_data.dropna()
    elif na_handling == "mean":
        numerical_data = numerical_data.fillna(numerical_data.mean())
    elif na_handling == "median":
        numerical_data = numerical_data.fillna(numerical_data.median())
    elif na_handling == "value":
        # Replace with a chosen value, for demonstration we use 0
        numerical_data = numerical_data.fillna(0)
    else:
        raise ValueError("na_handling must be 'drop', 'mean', 'median', or 'value'")

    # Use pandas built-in corr() method to get the correlation matrix
    correlation_matrix = numerical_data.corr()

    return correlation_matrix.astype(float)
