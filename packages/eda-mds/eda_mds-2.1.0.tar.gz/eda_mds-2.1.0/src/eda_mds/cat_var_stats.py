import pandas as pd
import numpy as np


def cat_var_stats(df, binning_threshold=2):
    """
    This function creates summary statistics about categorical variables in the dataframe. Number of unique values,
    frequency of values and whether some categories should binned will be among the info that will be presented.

    This function prints the following information about a DataFrame:
    - Number of unique values per categorical column.
    - Frequency of values for categorical columns.
    - Binning recommendations for low frequency values for categorical columns.


    Parameters
    ----------
    df : pandas.DataFrame
        A pandas dataframe.
    binning_threshold : int, optional
        A threshold for binning values. If a value has lower percentage frequency than the threshold it will be advised
        to bin them. The default is 2.

    Returns
    -------
    None :
        This function prints the following information and returns None.
    Example
    -------
    >>> import pandas as pd
    >>> df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
    >>> cat_var_stats(df)
    Column: sex
    Number of unique values: 2
    Frequency of values:
    male: 64.76%
    female: 35.24%
    ------------------------------------
    [...]
    Column: alone
    Number of unique values: 2
    Frequency of values:
    False: 39.73%
    True: 60.27%
    ------------------------------------
    """

    if type(df) != pd.DataFrame:
        raise TypeError("The input should be a pandas dataframe")
    if type(binning_threshold) != int and type(binning_threshold) != float:
        raise TypeError("The threshold value should be numeric")
    if binning_threshold < 0 or binning_threshold > 100:
        raise ValueError("The threshold value should be between 0 and 100")
    if df.empty:
        raise ValueError("The input dataframe should not be empty")

    for col in df.select_dtypes(include=['object', 'bool']).columns:  # iterate over categorical columns
        value_counts = dict()
        for val in df[col].unique():
            if pd.isna(val):
                value_counts[val] = (df[col].isna()).sum() / len(df) * 100
            else:
                value_counts[val] = (val == df[col]).sum() / len(df) * 100  # calculate frequency of values and save in dict
        if df[col].nunique() == len(df) or (np.array(list(value_counts.values())) < 1).sum() == df[col].nunique():
            continue  # if all values are unique or all values have frequency less than 1%, continue to next column
        print(f"Column: {col}")
        print(f"Number of unique values: {df[col].nunique()}")
        print("Frequency of values:")
        for val in df[col].unique():
            print(f"{val}: {value_counts[val]:.2f}%")
        if (np.array(list(value_counts.values())) < binning_threshold).sum() > 1:
            print("Binning recommendations:")
            low_freq_values = [str(k) for k, v in value_counts.items() if v < binning_threshold]

            print(', '.join(low_freq_values), 'values can be binned into "other" category as they are lower than'
                                              ' binning threshold')
        print("------------------------------------")
        print("\n")
