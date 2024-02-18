import pandas as pd
import numpy as np


def cat_var_stats(df, binning_threshold=2):
    """
    Generate summary statistics for categorical variables in a DataFrame.

    This function analyzes categorical columns in the provided DataFrame and
    prints out the number of unique values, the frequency of these values, and
    gives recommendations for binning low frequency categorical values based on
    a specified threshold.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame for which categorical variable stats are calculated.
    binning_threshold : int, optional
        The percentage frequency threshold below which categories will be
        recommended for binning. Default is 2.

    Returns
    -------
    None
        The function prints the statistics and returns None.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
    >>> cat_var_stats(df)
    Column: sex
    Number of unique values: 2
    Frequency of values:
    male: 64.76%
    female: 35.24%
    ------------------------------------

    """

    if type(df) != pd.DataFrame:  # Checks if input is a pandas dataframe
        raise TypeError("The input should be a pandas dataframe")
    if (
        type(binning_threshold) != int and type(binning_threshold) != float
    ):  # Checks if threshold is numeric
        raise TypeError("The threshold value should be numeric")
    if (
        binning_threshold < 0 or binning_threshold > 100
    ):  # Checks if threshold is between 0 and 100
        raise ValueError("The threshold value should be between 0 and 100")
    if df.empty:  # Checks if dataframe is empty
        raise ValueError("The input dataframe should not be empty")

    for col in df.select_dtypes(
        include=["object", "bool"]
    ).columns:  # iterate over categorical columns
        value_counts = dict()
        for val in df[col].unique():
            if pd.isna(val):
                value_counts[val] = (
                    (df[col].isna()).sum() / len(df) * 100
                )  # for na values calculate the frequency
            else:
                value_counts[val] = (
                    (val == df[col]).sum() / len(df) * 100
                )  # calculate frequency of values and save in dict
        if (
            df[col].nunique() == len(df)
            or (np.array(list(value_counts.values())) < 1).sum() == df[col].nunique()
        ):
            continue  # if all values are unique or all values have frequency less than 1%, continue to next column
        print(f"Column: {col}")
        print(f"Number of unique values: {df[col].nunique()}")
        print("Frequency of values:")
        for val in df[col].unique():
            print(f"{val}: {value_counts[val]:.2f}%")  # print frequency of values
        if (np.array(list(value_counts.values())) < binning_threshold).sum() > 1:
            print("Binning recommendations:")
            low_freq_values = [
                str(k) for k, v in value_counts.items() if v < binning_threshold
            ]

            print(
                ", ".join(low_freq_values),
                'values can be binned into "other" category as they are lower than'
                " binning threshold",
            )
        print("------------------------------------")
        print("\n")
