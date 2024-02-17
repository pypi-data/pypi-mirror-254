import pandas as pd

def describe_outliers(df, threshold=1.5, numeric=True):
    """
    Extends the functionality of pandas.Dataframe.describe() for numeric data by 
    additionally providing a count of lower-tail and upper-tail outliers. 

    If the data contains numerical values the printed description includes the following
    information:
    
    - dtype: the datatype of the column. 
    - Non-null count: The number of non-null observations.
    - mean: The mean value.
    - standard deviation: The standard deviation.
    - min: the minimum value.
    - 25% percentile: The 25% percentile (Q1).
    - 50% (median): The 50% percentile (Q2).
    - 75% percentile: The 75% percentile (Q3).
    - max: the maximum value.
    - lower-tail outliers: count of values significantly smaller than the majority of data.
    - upper-tail outliers: count of values significantly larger than the majority of data.

    The number of outliers is calculated using the Interquartile Range (IQR) 
    method for outlier detection. Lower-tail outliers are observations less than:
    Q1 - threshold*IQR. Upper-tail outliers are observations greater than: Q3 + threshold*IQR. 

    Parameters
    ----------
    df : pandas.DataFrame
        A tidy dataframe containing at least 1 numeric column. 
    
    threshold : float, optional
        The scalar used in outlier detection. It must be a non-negative numeric value. A higher 
        value reduces the sensitivity of outlier detection. Default is 1.5 
    
    numeric : boolean, optional
        If set to True, the returned dataframe will only include description on numeric columns. 
        If False, the output will include the dtype and count for non-numeric columns. Default is True.  

    Returns
    -------
    summary_df : pandas.DataFrame
        A dataframe of the descriptive summary statistics. 
    
    Example
    --------
    >>>  import pandas as pd
    >>>  data = {'numeric': [1, 2, 3, 4, 5, 100], 
    >>>         'categorical': ['a', 'b', 'c', 'd', 'e', 'f']}
    >>>  df = pd.DataFrame(data)
    >>>  describe_outliers(df, threshold = 2, numeric=False)
    # Output 
                        categorical	    numeric
        dtype	            object	    int64
        Non-null count	    6	        6
        mean	            NaN	        19.166667
        standard deviation	NaN	        39.625329
        min value	        NaN	        1.0
        25% percentile	    NaN	        2.25
        50% (median)	    NaN	        3.5
        75% percentile	    NaN	        4.75
        max value	        NaN	        100.0
        lower-tail outliers	NaN	        0.0
        upper-tail outliers	NaN	        1.0
    """
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input df must be a DataFrame.")

    if not threshold >= 0:
        raise ValueError("Invalid value for threshold. Threshold must be a non-negative number.")
    
    column_names = df.columns
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    # consider only numeric columns (unless specified)
    if numeric == True:
        column_names = numeric_columns

    if len(numeric_columns) == 0:
        raise ValueError("Your dataframe contains no numeric columns. It should include at least 1.")
    
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
    lower_fences = q1 - threshold*iqr
    upper_fences = q3 + threshold*iqr
    lower_outliers_count = (df[numeric_columns] < lower_fences).sum()
    upper_outliers_count = (df[numeric_columns] > upper_fences).sum()

    # display the description
    summary_df = pd.DataFrame({
        'dtype': df.dtypes[column_names],
        'Non-null count': counts,
        'mean': mean,
        'standard deviation': sd,
        'min value': min,
        '25% percentile': q1,
        '50% (median)': q2,
        '75% percentile': q3,
        'max value': max,
        'lower-tail outliers': lower_outliers_count,
        'upper-tail outliers': upper_outliers_count
    }).T
    
    return summary_df


    