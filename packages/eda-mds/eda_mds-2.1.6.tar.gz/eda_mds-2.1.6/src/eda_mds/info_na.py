import numpy as np
import pandas as pd
import warnings


def info_na(df):
    """
    Extend pandas.DataFrame.info() with row-level null value statistics.

    This function enhances the DataFrame.info() method by adding a summary of null
    values at the row level. It prints type, shape, memory usage, and column information,
    along with new statistics such as the count and percentage of null values in rows,
    providing a comprehensive characterization of the DataFrame's structure.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be analyzed for null value statistics.

    Returns
    -------
    None
        The function prints detailed descriptive information to the console and returns None.

    Examples
    --------
    >>> df_example = pd.DataFrame(
            [
                [np.nan, 13, "hello"],
                [np.nan, np.nan, "this"],
                [37, 45, "is"],
                [256, 31, ""],
                [1, np.nan, "test"],
            ],
            index=["First", "Second", "Third", "Fourth", "Fifth"],
            columns=["Column1", "ColumnNumber2", "Column3"],
        )
    >>> info_na(df_example)
    # Expected output format:
    type: <class 'pandas.core.frame.DataFrame'>
    shape: (5, 3)
    memory usage: 692 B
    ...
    """

    # Input checks and warnings
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input `df` must be a Pandas DataFrame")

    if pd.isna(df).all(axis=None):
        warnings.warn("Input `df` contains all NA values")

    # Collect information about df
    type_info = type(df)

    shape_info = df.shape

    column_info = pd.DataFrame(
        {
            "#": np.arange(df.shape[1]),
            "column": df.columns.values,
            "null count": df.isna().sum(axis=0),
            "null %": (df.isna().sum(axis=0) / df.shape[0] * 100).round(2),
            "dtype": df.dtypes,
        }
    )

    row_info = pd.Series(
        {
            "total rows": df.shape[0],
            "any null count": df.isna().any(axis=1).sum(),
            "any null %": (df.isna().any(axis=1).sum() / df.shape[0] * 100).round(2),
            "all null count": df.isna().all(axis=1).sum(),
            "all null %": (df.isna().all(axis=1).sum() / df.shape[0] * 100).round(2),
            "mean null count": df.isna().sum(axis=1).mean().round(2),
            "std.dev null count": df.isna().sum(axis=1).std().round(2),
            "max null count": df.isna().sum(axis=1).max(),
            "min null count": df.isna().sum(axis=1).min(),
        }
    )

    # Human-readable memory usage formatting
    suffix = ["B", "KB", "MB", "GB", "TB"]
    memory_bytes = df.memory_usage(deep=True).sum()
    n = 0
    while memory_bytes > 2**10:
        memory_bytes = memory_bytes / 2**10
        n += 1
    memory_info = f"{np.round(memory_bytes, 1)} {suffix[n]}"

    # Format to output string
    output = f"""
type: {type_info}
shape: {shape_info}
memory usage: {memory_info}
--------
columns:
{column_info.to_string(index=False)}
-----
rows:
{row_info.to_string()}
"""

    print(output)
