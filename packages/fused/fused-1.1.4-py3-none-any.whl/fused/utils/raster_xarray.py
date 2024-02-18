from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
import xarray
from affine import Affine

from fused.api import FusedAPI

from ._rasterize_geometry import rasterize_geometry
from .raster_numpy import (
    get_raster_numpy,
    get_raster_numpy_from_chips,
    get_raster_numpy_grouped,
)


def shape_to_xy(
    shape: Union[Tuple[int, int], Tuple[int, int, int]], transform: Affine
) -> Tuple[List[float], List[float]]:
    """Convert a 2D or 3D shape to arrays of x and y coordinates

    Args:
        shape: The 2-dimensional or 3-dimensional shape of the image. Either (rows, columns) or (bands, rows, columns).
        transform: An Affine transform describing the given image.

    Returns:
        A two-tuple each containing a list of floats. The first represents the x coordinates and the second the y coordinates.
    """
    # todo: handle 3 bands and their name
    height = shape[-2]
    width = shape[-1]
    dx = transform[0]
    dy = transform[4]
    x_coor = transform[2]
    y_coor = transform[5]

    # Note: this is half a pixel so that the x and y coordinates are in the centers of
    # each pixel
    x_pixel_offset = dx / 2
    y_pixel_offset = dy / 2

    x = [x_coor + (i * dx) + x_pixel_offset for i in range(width)]
    y = [y_coor + (j * dy) + y_pixel_offset for j in range(height)]
    return x, y


def rows_to_xarray(
    rows: pd.DataFrame,
    group_by: Sequence[str] = ("asset_name"),
    dim_col: str = "datetime",
    sort_by_dim: bool = True,
    mosaic_cols: Optional[Iterable[str]] = None,
    merge: Optional[Dict[str, Any]] = {"compat": "override"},
) -> Union[xarray.Dataset, List[xarray.Dataset]]:
    """Convert raster chips to an xarray Dataset

    Args:
        rows: A DataFrame of raster chips to convert to xarray
        group_by: The column(s) in `rows` to group on. Defaults to ("asset_name").
        dim_col: The column used as the third dimension in the xarray Dataset. Defaults to "datetime".
        sort_by_dim: Sort the Dataset by the `dim_col`. Defaults to True.
        mosaic_cols: Other columns to group on. Defaults to None.
        merge: Keyword arguments to pass to [`xarray.merge`][xarray.merge]. Defaults to `{"compat": "override"}`.

    Returns:
        An xarray dataset with chip information.
    """
    # TODO: For `merge`, make it immutable
    L_names = len(group_by)
    group_by = [*group_by]
    if mosaic_cols:
        group_by.extend(mosaic_cols)

    gb = rows.groupby(group_by)
    arr_ds = []

    for name, rows in iter(gb):
        if isinstance(name, str):
            asset_name = name
        elif L_names == 1:
            asset_name = name[0]
        else:
            asset_name = "_".join([str(i) for i in name[:L_names]])
        row = rows.iloc[0]
        x, y = shape_to_xy(row["shape"], row["transform"])
        # TODO: Something is wrong with using this with NAIP because it has multiple bands
        array_data = np.vstack([v.array_data for _, v in rows.iterrows()])
        array_mask = np.vstack([v.array_mask for _, v in rows.iterrows()])
        if dim_col == "datetime":
            dim_col_data = pd.to_datetime(rows[dim_col])
        else:
            dim_col_data = rows[dim_col]
        coords = {dim_col: dim_col_data.values, "y": y, "x": x}
        attrs = row[
            [
                "filepath",
                "datetime",
                "shape",
                "transform",
                "crs",
                "projected_geom",
                "fused_index",
            ]
        ].to_dict()
        ds = xarray.Dataset(
            data_vars={
                asset_name: xarray.DataArray(array_data, coords=coords, attrs=attrs),
                "mask_"
                + asset_name: xarray.DataArray(array_mask, coords=coords, attrs=attrs),
            }
        )
        if sort_by_dim:
            ds = ds.sortby(dim_col)
        arr_ds.append(ds)

    if merge:
        return xarray.merge(arr_ds, **merge)
    else:
        return arr_ds


def get_raster_xarray(
    left,
    right,
    *,
    xarray_group_by: Sequence[str] = ("asset_name",),
    xarray_dim_col: str = "datetime",
    xarray_sort_by_dim: bool = True,
    xarray_mosaic_cols: Optional[Iterable[str]] = None,
    xarray_merge: Optional[Dict[str, Any]] = {"compat": "override"},
    asset_names: Sequence[str],
    n_rows: Optional[int] = None,
    prefetch_entire_files: bool = False,
    buffer: Optional[float] = None,
    href_modifier: Optional[Callable[[str], str]] = None,
    href_mapping: Optional[Dict[str, str]] = None,
    context: None = None,
    api: Optional[FusedAPI] = None,
    _fetch_all_at_once: bool = True,
    **kwargs,
) -> Union[xarray.Dataset, List[xarray.Dataset]]:
    """Get a raster as an xarray Dataset

    Args:
        left: The input join object with geometries.
        right: The input join object with STAC data.

    Keyword Args:
        xarray_group_by: The column(s) in the numpy raster items to group on. Defaults to ("asset_name").
        xarray_dim_col: The column name to use as the xarray dimension column. Defaults to "datetime".
        xarray_sort_by_dim: Sort by the xarray dimension column. Defaults to True.
        xarray_mosaic_cols:
        xarray_merge: Keyword arguments to pass to [`xarray.merge`][xarray.merge]. Defaults to `{"compat": "override"}`.
        asset_names: The name(s) of assets in the STAC data to use.
        n_rows: A limit to the number of rows used from the left side. Defaults to None.
        prefetch_entire_files: If True, on the backend will fetch entire files to the local machine instead of doing partial reads from S3. Defaults to False.
        buffer: If set, will buffer the data by this amount before fetching the raster data. Note that this buffer happens after the join between left and right. Defaults to None.
        href_modifier: A function to modify asset hrefs before fetching. Defaults to None.
        href_mapping: A dictionary from `str` to `str` that specifies how to change asset hrefs before fetching data. Note that `href_modifier` is applied after `href_mapping`. Defaults to None.
        context: Unused in the local `fused` version. On the server this has context information. Defaults to None.
        api: An instance of `FusedAPI` to use for interacting with the backend. Defaults to None.
        _fetch_all_at_once: If True, will parallelize downloads. Defaults to False.

    Yields:
        A dictionary of records with each row's information.
    """
    # TODO: For `xarray_merge`, make it immutable
    rows = get_raster_numpy(
        left=left,
        right=right,
        asset_names=asset_names,
        n_rows=n_rows,
        prefetch_entire_files=prefetch_entire_files,
        buffer=buffer,
        href_modifier=href_modifier,
        href_mapping=href_mapping,
        additional_columns=xarray_group_by,
        context=context,
        api=api,
        _fetch_all_at_once=_fetch_all_at_once,
        **kwargs,
    )

    df2 = pd.DataFrame.from_records([row for row in rows])

    return rows_to_xarray(
        df2,
        group_by=xarray_group_by,
        dim_col=xarray_dim_col,
        sort_by_dim=xarray_sort_by_dim,
        mosaic_cols=xarray_mosaic_cols,
        merge=xarray_merge,
    )


def get_raster_xarray_grouped(
    left,
    right,
    *,
    xarray_group_by: Sequence[str] = ("asset_name",),
    xarray_dim_col: str = "datetime",
    xarray_sort_by_dim: bool = True,
    xarray_mosaic_cols: Optional[Iterable[str]] = None,
    xarray_merge: Optional[Dict[str, Any]] = {"compat": "override"},
    group_by: Sequence[str] = ("orig_file_index", "orig_row_index"),
    asset_names: Sequence[str],
    n_rows: Optional[int] = None,
    prefetch_entire_files: bool = False,
    buffer: Optional[float] = None,
    href_modifier: Optional[Callable[[str], str]] = None,
    href_mapping: Optional[Dict[str, str]] = None,
    context: None = None,
    api: Optional[FusedAPI] = None,
    _fetch_all_at_once: bool = True,
    **kwargs,
) -> Iterable[Union[xarray.Dataset, List[xarray.Dataset]]]:
    """Get a raster as an xarray Dataset

    Args:
        left: The input join object with geometries.
        right: The input join object with STAC data.

    Keyword Args:
        xarray_group_by:
        xarray_dim_col: The column name to use as the xarray dimension column. Defaults to "datetime".
        xarray_sort_by_dim: Sort by the xarray dimension column. Defaults to True.
        xarray_mosaic_cols:
        xarray_merge: Keyword arguments to pass to [`xarray.merge`][xarray.merge]. Defaults to `{"compat": "override"}`.
        group_by: The column(s) to group on.
        asset_names: The name(s) of assets in the STAC data to use.
        n_rows: A limit to the number of rows used from the left side. Defaults to None.
        prefetch_entire_files: If True, on the backend will fetch entire files to the local machine instead of doing partial reads from S3. Defaults to False.
        buffer: If set, will buffer the data by this amount before fetching the raster data. Note that this buffer happens after the join between left and right. Defaults to None.
        href_modifier: A function to modify asset hrefs before fetching. Defaults to None.
        href_mapping: A dictionary from `str` to `str` that specifies how to change asset hrefs before fetching data. Note that `href_modifier` is applied after `href_mapping`. Defaults to None.
        context: Unused in the local `fused` version. On the server this has context information. Defaults to None.
        api: An instance of `FusedAPI` to use for interacting with the backend. Defaults to None.
        _fetch_all_at_once: If True, will parallelize downloads. Defaults to False.

    Yields:
        An xarray Dataset per group
    """
    # TODO: For `xarray_merge`, make it immutable
    groups = get_raster_numpy_grouped(
        left=left,
        right=right,
        group_by=group_by,
        asset_names=asset_names,
        n_rows=n_rows,
        prefetch_entire_files=prefetch_entire_files,
        buffer=buffer,
        href_modifier=href_modifier,
        href_mapping=href_mapping,
        context=context,
        api=api,
        _fetch_all_at_once=_fetch_all_at_once,
        **kwargs,
    )

    for group in groups:
        yield rows_to_xarray(
            group,
            group_by=xarray_group_by,
            dim_col=xarray_dim_col,
            sort_by_dim=xarray_sort_by_dim,
            mosaic_cols=xarray_mosaic_cols,
            merge=xarray_merge,
        )


def get_raster_xarray_from_chips(
    input,
    *,
    sidecar_table_name: str,
    xarray_group_by: Sequence[str] = ("asset_name",),
    xarray_dim_col: str = "datetime",
    xarray_sort_by_dim: bool = True,
    xarray_mosaic_cols: Optional[Iterable[str]] = None,
    xarray_merge: Optional[Dict[str, Any]] = {"compat": "override"},
    n_rows: Optional[int] = None,
    **kwargs,
) -> Union[xarray.Dataset, List[xarray.Dataset]]:
    """Get numpy array from chips

    Args:
        input: The input object prejoined geometry and STAC data.
        sidecar_table_name: The name of the table in `input` that contains chips as its sidecar file.
        xarray_group_by:
        xarray_dim_col: The column name to use as the xarray dimension column. Defaults to "datetime".
        xarray_sort_by_dim: Sort by the xarray dimension column. Defaults to True.
        xarray_mosaic_cols:
        xarray_merge: Keyword arguments to pass to [`xarray.merge`][xarray.merge]. Defaults to `{"compat": "override"}`.
        n_rows: The number of chips to load from the sidecar. Defaults to None, which loads all chips.

    Returns:
        xarray Dataset containing chip data.
    """
    # TODO: For `xarray_merge`, make it immutable
    rows = get_raster_numpy_from_chips(
        input=input,
        sidecar_table_name=sidecar_table_name,
        n_rows=n_rows,
        **kwargs,
    )

    df2 = pd.DataFrame.from_records([row for row in rows])

    return rows_to_xarray(
        df2,
        group_by=xarray_group_by,
        dim_col=xarray_dim_col,
        sort_by_dim=xarray_sort_by_dim,
        mosaic_cols=xarray_mosaic_cols,
        merge=xarray_merge,
    )


def rasterize_geometry_xarray(
    xds: xarray.Dataset, scale: float = 10, all_touched: bool = False
) -> xarray.Dataset:
    """Create an Xarray Dataset with the geometry.

    Args:
      xds: Dataset to take geometry, transform, and shape attributes from.
      scale: Scale factor to apply when computing geometry weights. Higher values use more pixels to calculate the weight.
      all_touched: rasterization strategy. Defaults to False.

    Returns:
      xarray Dataset containing geometry weights, or NaN where the geometry does not intersect.
    """
    shape = xds.asset.attrs["shape"][1:]
    shape[0] *= scale
    shape[1] *= scale
    aff = xds.asset.attrs["transform"]
    transform = Affine(aff[0] / scale, aff[1], aff[2], aff[3], aff[4] / scale, aff[5])
    geom_mask = rasterize_geometry(
        geom=xds.asset.attrs["projected_geom"],
        shape=shape,
        affine=transform,
        all_touched=all_touched,
    )
    x, y = shape_to_xy(shape, transform)
    coords = {"y": y, "x": x}
    geom_xarray = (
        xarray.DataArray(geom_mask, coords=coords).coarsen(x=scale, y=scale).mean()
    )
    return geom_xarray.where(geom_xarray > 0, np.nan)
