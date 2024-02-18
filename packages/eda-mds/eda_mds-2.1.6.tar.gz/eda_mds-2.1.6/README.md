# eda_mds: Simplified Exploratory Data Analysis
 
[![Documentation Status](https://readthedocs.org/projects/eda-mds/badge/?version=latest)](https://eda-mds.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
![version](https://img.shields.io/github/v/release/UBC-MDS/eda_mds)
![release](https://img.shields.io/github/release-date/UBC-MDS/eda_mds)
---

Basic EDA functions implemented to improve on core Pandas DataFrame functions.

## Summary

This package is created for kick-starting the EDA stage of a machine learning and analytics project. 
It's primary objective is to improve upon the popular EDA functions present in `pandas` package. 
There are four functions that deliver insights and identify potential problems in the dataset. 

### Function Descriptions
- `cor_eda`: This function accepts a dataset and isolates its numerical continuous variables. 
It calculates the correlation between each numerically continuous variable from scratch and displays the results in a table.
- `info_na`: This function replicates and extends behaviour of [pandas.DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html). 
Additional information about null values in rows and columns is included. 
- `cat_var_stats`: This function creates summary statistics about categorical variables in the dataframe. 
Number of unique values, frequency of values, and suggested category binning is included.
- `describe_outliers`: This function extends the functionality of [pandas.Dataframe.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) for numeric data by providing a count of lower-tail and upper-tail outliers for a given threshold.

### Python Ecosystem Integration

Our functions are heavily inspired from [`pandas`](https://github.com/pandas-dev/pandas) package for python. 
EDA functions such as `pandas.Dataframe.info`, `pandas.Dataframe.describe` and `pandas.Dataframe.corr` are recreated and improved upon in this package.
Our functions also depend on the `pandas.Dataframe` object.

## Installation

### User Setup

This package can be installed via PyPi by running the following command in your terminal.

```console
$ pip install eda_mds
```

### Developer Setup

Here's how to install `eda_mds` for local development.

1. Clone a copy of `eda_mds` locally, by running the following command in your terminal.
    ```console
    $ git clone https://github.com/UBC-MDS/eda_mds.git
    ```
2. Create/activate new `conda` environment and install poetry.

    ```console
    $ conda create -n eda_mds_dev python=3.9 poetry
    ```

    ```console
    $ conda activate eda_mds_dev 
    ```
4. Navigate to the root directory.
    ```console
    $ cd path/to/eda_mds
    ```

3. Install `eda_mds` using `poetry`.

    ```console
    $ poetry install
    ```

## Running the Tests and Coverage
1. To run the tests navigate to the root directory. 
    ```console
    $ cd path/to/eda_mds
    ```
2. To run the tests navigate to the root directory.
    ```console
    $ pytest
    ```
3. To run the coverage report.
    ```console
    $ coverage report
    ```     

## Usage

### Function Usage

Below provides a short depiction on how to start using the functions in this package, after you have completed the installation. Please see the [vingette](https://eda-mds.readthedocs.io/en/latest/example.html) for detailed usage. Note: Each function takes in a `pandas.DataFrame` object.

1. Import the functions and [`pandas`](https://github.com/pandas-dev/pandas).

```python
from eda_mds import info_na, describe_outliers, cat_var_stats, cor_eda

import pandas as pd
```
2. Load your dataset of choice. 

```python
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
```

3. Begin using the functions! 

```python
info_na(df)
```
```python
describe_outliers(df)
```
```python
cat_var_stats(df)
```
```python
cor_eda(df)
```

## Contributing
Package created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew.

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). 
Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`eda_mds` was created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew. 
Code is licensed under the terms of the MIT license. 
Non-code portions, specifically vignettes and related documentation, is licensed under the terms of the Creative Commons Zero v1.0 Universal license.

## Credits

`eda_mds` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
