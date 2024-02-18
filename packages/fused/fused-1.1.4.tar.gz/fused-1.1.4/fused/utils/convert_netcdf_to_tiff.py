from typing import Optional, Sequence, Union

import rasterio.transform
import xarray
from affine import Affine
from loguru import logger

try:
    import rioxarray

    _has_rio_xarray = True
except ImportError:
    _has_rio_xarray = False


def netcdf_to_tiff(
    inpath: str,
    outpath,
    variable,
    transform: Union[Sequence[float], Affine, None] = None,
    crs=None,
    xy_dims=None,
    driver: Optional[str] = "COG",
) -> None:
    """Convert NetCDF to GeoTIFF

    Args:
        inpath: The source NetCDF file to load.
        outpath: The output location of the new GeoTIFFs.
        variable: The variable of the input dataset to write as output.
        transform: The affine transformation matrix of the data to include when writing. Defaults to None.
        crs: The Coordinate Reference System to write on the data. Defaults to None.
        xy_dims: _description_. Defaults to None.
        driver: The GDAL driver to use when saving data. Defaults to "COG".
    """

    def _read_with_xarray():
        logger.debug("Opening using open_dataset")
        return xarray.open_dataset(inpath, decode_coords="all")[variable]

    if _has_rio_xarray:
        try:
            da = rioxarray.open_rasterio(inpath, decode_coords="all")[variable]
            logger.debug("Opening using open_rasterio")
        except:  # noqa: E722
            da = _read_with_xarray()
    else:
        da = _read_with_xarray()
    if xy_dims:
        da = da.rio.set_spatial_dims(*xy_dims)
    if crs:
        da = da.rio.write_crs(crs)
    if da.rio.crs is None:
        raise ValueError("No crs found. Please manually specify the crs.")
    if transform:
        if isinstance(transform, Sequence):
            transform = rasterio.transform.Affine(*transform)
        da = da.rio.write_transform(transform)
    da.rio.to_raster(outpath, driver=driver)
    da.close()
