import pandas as pd


def describe_outliers(df, threshold=1.5, numeric=True):
    """
    Enhance pandas.DataFrame.describe() with outlier counts for numeric columns.

    This function extends the output of pandas.DataFrame.describe() by counting
    and including lower-tail and upper-tail outliers for each numeric column in the DataFrame.
    The outlier count is determined using the Interquartile Range (IQR) method, with a
    customizable threshold for defining what constitutes an outlier.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame with at least one numeric column.
    threshold : float, optional
        A non-negative scalar that adjusts the sensitivity of outlier detection.
        A higher value decreases the sensitivity. The default is 1.5.
    numeric : bool, optional
        If True, only numeric columns are included in the output. If False, the output
        includes the dtype and count for non-numeric columns as well. The default is True.

    Returns
    -------
    pandas.DataFrame
        A DataFrame summarizing the descriptive statistics and including outlier counts.

    Examples
    --------
    >>> import pandas as pd
    >>> data = {'numeric': [1, 2, 3, 4, 5, 100],
                 'categorical': ['a', 'b', 'c', 'd', 'e', 'f']}
    >>> df = pd.DataFrame(data)
    >>> describe_outliers(df, threshold=2, numeric=False)
    # Output will display the DataFrame with the descriptive statistics and outlier counts.

    Notes
    -----
    Lower-tail outliers are calculated as values less than Q1 - (threshold * IQR).
    Upper-tail outliers are calculated as values greater than Q3 + (threshold * IQR).

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input df must be a DataFrame.")

    if not threshold >= 0:
        raise ValueError(
            "Invalid value for threshold. Threshold must be a non-negative number."
        )

    column_names = df.columns
    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    # consider only numeric columns (unless specified)
    if numeric == True:
        column_names = numeric_columns

    if len(numeric_columns) == 0:
        raise ValueError(
            "Your dataframe contains no numeric columns. It should include at least 1."
        )

    # calculate summary statistics
    counts = df[column_names].count().astype(int)
    mean = df[numeric_columns].mean()
    sd = df[numeric_columns].std()
    min = pd.Series(df[numeric_columns].min(), index=numeric_columns)
    q1 = df[numeric_columns].quantile(0.25)
    q2 = df[numeric_columns].quantile(0.50)
    q3 = df[numeric_columns].quantile(0.75)
    max = pd.Series(df[numeric_columns].max(), index=numeric_columns)

    # outlier detection
    iqr = q3 - q1
    lower_fences = q1 - threshold * iqr
    upper_fences = q3 + threshold * iqr
    lower_outliers_count = (df[numeric_columns] < lower_fences).sum()
    upper_outliers_count = (df[numeric_columns] > upper_fences).sum()

    # display the description
    summary_df = pd.DataFrame(
        {
            "dtype": df.dtypes[column_names],
            "Non-null count": counts,
            "mean": mean,
            "standard deviation": sd,
            "min value": min,
            "25% percentile": q1,
            "50% (median)": q2,
            "75% percentile": q3,
            "max value": max,
            "lower-tail outliers": lower_outliers_count,
            "upper-tail outliers": upper_outliers_count,
        }
    ).T

    return summary_df
