import logging
import pathlib

import xarray
import zarr
from dask.delayed import Delayed
from tqdm.dask import TqdmCallback

from copernicus_marine_client.core_functions.exceptions import (
    NetCDFCompressionNotAvailable,
)

logger = logging.getLogger("copernicus_marine_root_logger")


def get_delayed_download(
    dataset: xarray.Dataset,
    output_path: pathlib.Path,
    netcdf_compression_enabled: bool,
):
    if output_path.suffix == ".nc":
        delayed = _prepare_download_dataset_as_netcdf(
            dataset, output_path, netcdf_compression_enabled
        )
    elif output_path.suffix == ".zarr":
        if netcdf_compression_enabled:
            raise NetCDFCompressionNotAvailable(
                "--netcdf-compression-enabled option cannot be used when"
                "writing to ZARR"
            )
        delayed = _prepare_download_dataset_as_zarr(dataset, output_path)
    else:
        delayed = _prepare_download_dataset_as_netcdf(
            dataset, output_path, netcdf_compression_enabled
        )
    return delayed


def download_delayed_dataset(
    delayed: Delayed, disable_progress_bar: bool
) -> None:
    if disable_progress_bar:
        delayed.compute()
    else:
        with TqdmCallback():
            delayed.compute()


def _prepare_download_dataset_as_netcdf(
    dataset: xarray.Dataset,
    output_path: pathlib.Path,
    netcdf_compression_enabled: bool,
):
    logger.debug("Writing dataset to NetCDF")
    if netcdf_compression_enabled:
        logger.debug("NetCDF compression enabled")
        comp = dict(zlib=True, complevel=1, contiguous=False, shuffle=True)
        encoding = {var: comp for var in dataset.data_vars}
    else:
        encoding = None
    return dataset.to_netcdf(
        output_path, mode="w", compute=False, encoding=encoding
    )


def _prepare_download_dataset_as_zarr(
    dataset: xarray.Dataset, output_path: pathlib.Path
):
    logger.debug("Writing dataset to Zarr")
    store = zarr.DirectoryStore(output_path)
    return dataset.to_zarr(store=store, mode="w", compute=False)
