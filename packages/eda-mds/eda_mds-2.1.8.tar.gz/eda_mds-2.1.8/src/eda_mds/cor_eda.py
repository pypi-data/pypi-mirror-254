import pandas as pd
import numpy as np


def cor_eda(dataset, na_handling="drop"):
    """
    Calculate the correlation between numerical variables in a DataFrame.

    This function processes a given DataFrame to isolate numerical variables,
    handles missing values according to the specified method, calculates the
    correlation between each pair of numerical variables, and returns the results
    in a new DataFrame.


    Parameters
    ----------
    dataset : DataFrame
        The DataFrame to be analyzed. It should include a variety of variable types.
    na_handling : str, optional
        Method for handling missing values (NAs). The following options are available:
        - 'drop': Drop rows with any NAs (default).
        - 'mean': Replace NAs with the mean value of the column.
        - 'median': Replace NAs with the median value of the column.


    Returns
    -------
    DataFrame
        A DataFrame containing the correlation coefficients between each pair of
        numerical variables.

    Examples
    --------
    >>> cor_eda(data, na_handling='mean')
             age    salary
    age     1.0000   0.9769
    salary  0.9769   1.0000

    """
    # Isolate the numerical variables
    numerical_data = dataset.select_dtypes(include=["number"])

    if numerical_data.empty:
        return "no numerical columns found"

    # Handle missing values according to the specified method
    if na_handling == "drop":
        numerical_data = numerical_data.dropna()
    elif na_handling == "mean":
        numerical_data = numerical_data.fillna(numerical_data.mean())
    elif na_handling == "median":
        numerical_data = numerical_data.fillna(numerical_data.median())
    else:
        raise ValueError("na_handling must be 'drop', 'mean', 'median'")

    # Use pandas built-in corr() method to get the correlation matrix
    correlation_matrix = numerical_data.corr()

    return correlation_matrix.astype(float)
