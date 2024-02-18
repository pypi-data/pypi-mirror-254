"""
.
"""

from importlib.metadata import version
import pathlib

import json
import logging.config
import time

__version__ = version("copernicus-marine-client")

log_configuration_dict = json.load(
    open(
        pathlib.Path(
            pathlib.Path(__file__).parent, "logging_conf.json"
        )
    )
)
logging.config.dictConfig(log_configuration_dict)
logging.Formatter.converter = time.gmtime

logger = logging.getLogger("copernicus_marine_root_logger")

logger.warning("!! This version has been deprecated and is no longer maintained !!")
logger.warning("A new package has been released to replace it. You can find it here: https://pypi.org/project/copernicusmarine/")
logger.warning("Or install it using the following command: `pip install copernicusmarine`")

from copernicus_marine_client.python_interface.login import login
from copernicus_marine_client.python_interface.describe import describe
from copernicus_marine_client.python_interface.get import get
from copernicus_marine_client.python_interface.subset import subset
from copernicus_marine_client.python_interface.open_dataset import open_dataset
from copernicus_marine_client.python_interface.open_dataset import load_xarray_dataset  # depracated
from copernicus_marine_client.python_interface.read_dataframe import read_dataframe
from copernicus_marine_client.python_interface.read_dataframe import load_pandas_dataframe  # depracated
