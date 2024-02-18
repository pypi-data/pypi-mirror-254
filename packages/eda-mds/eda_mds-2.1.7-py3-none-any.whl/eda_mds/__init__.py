# read version from installed package
from importlib.metadata import version
__version__ = version("eda_mds")

from eda_mds.info_na import info_na
from eda_mds.cat_var_stats import cat_var_stats
from eda_mds.cor_eda import cor_eda
from eda_mds.describe_outliers import describe_outliers