# eda_mds: Simplified Exploratory Data Analysis
 
[![Documentation Status](https://readthedocs.org/projects/eda-mds/badge/?version=latest)](https://eda-mds.readthedocs.io/en/latest/?badge=latest)
---

Basic EDA functions implemented to improve on core Pandas DataFrame functions.

## Installation

This project has not yet been uploaded to PyPI. 
Please see [contributing](CONTRIBUTING.md) for instructions to install locally. 

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


## Usage

### Installation
This project has not yet been uploaded to PyPI. 
Please see [contributing](CONTRIBUTING.md) for instructions to install locally. 

### Function Usage
Each function takes a `pandas.DataFrame` object. 
Please see the included vingette for intended use. 

## Contributing
Package created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew.

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). 
Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`eda_mds` was created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew. It is licensed under the
terms of the MIT license.

## Credits

`eda_mds` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
