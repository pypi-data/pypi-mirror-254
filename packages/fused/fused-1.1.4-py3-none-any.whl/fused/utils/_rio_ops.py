from __future__ import annotations

import sys

import numpy as np
import rasterio
import shapely
import xarray
from affine import Affine
from scipy.ndimage import zoom
from scipy.spatial import KDTree

__all__ = (
    "rio_distance",
    "rio_resample",
    "rio_super_resolution",
    "rio_scale_shape_transform",
    "rio_geom_to_xy_slice",
)


def rio_distance(
    dataset: xarray.Dataset,
    variable: str,
    suffix: str = "_distance",
    coords_x: str = "x",
    coords_y: str = "y",
    chunk_size: int = 500_000,
    verbose: bool = False,
) -> xarray.Dataset:
    df = dataset[variable].to_dataframe().reset_index()
    df2 = df[df[variable] == 1]
    if len(df2) == 0:
        return xarray.DataArray(
            dataset[variable].values + np.inf,
            name=variable + suffix,
            coords=dataset[variable].coords,
        )
    tree = KDTree(np.vstack(list(zip(df2[coords_x].values, df2[coords_y].values))))
    df["dist"] = 0
    n_chunk = (len(df) // chunk_size) + 1
    for i in range(n_chunk):
        if verbose:
            sys.stdout.write(f"\r{i+1} of {n_chunk}")
        tmp = df.iloc[i * chunk_size : (i + 1) * chunk_size]
        distances, indices = tree.query(
            np.vstack(list(zip(tmp[coords_x].values, tmp[coords_y].values))), k=1
        )
        df.iloc[
            i * chunk_size : (i + 1) * chunk_size, -1
        ] = distances  # [:,-1] guarantees [:,'dist']
    if verbose:
        print(" done!")
    return xarray.DataArray(
        df.dist.values.reshape(dataset[variable].shape),
        name=variable + suffix,
        coords=dataset[variable].coords,
    )


def rio_resample(
    da1, da2, method="linear", reduce="mean", factor=None, order=1, verbose=True
):
    if da1.shape[0] >= da2.shape[0]:
        if not factor:
            factor = int(np.ceil(da1.shape[0] / da2.shape[0]))
        if verbose:
            print(f"downsampling: {reduce=}, {factor=}")
        return (
            da1.interp(
                x=zoom(da2.x, factor, order=order),
                y=zoom(da2.y, factor, order=order),
                method=method,
            )
            .coarsen(x=factor, y=factor)
            .reduce(reduce)
        )
    else:
        if verbose:
            print("upsampling: reduce & factor is not used")
        return da1.interp_like(da2, method="linear")


def rio_super_resolution(da, factor=2, dims=("x", "y"), method="linear", order=1):
    return da.interp({d: zoom(da[d], factor, order=order) for d in dims}, method=method)


def rio_scale_shape_transform(shape, transform, factor=10):
    (
        pixel_width,
        row_rot,
        x_upper_left,
        col_rot,
        pixel_height,
        y_upper_left,
    ) = transform[:6]
    transform = Affine(
        pixel_width / factor,
        row_rot,
        x_upper_left,
        col_rot,
        pixel_height / factor,
        y_upper_left,
    )
    shape = list(shape[-2:])
    shape[0] = shape[0] * factor
    shape[1] = shape[1] * factor
    return shape, transform


def rio_geom_to_xy_slice(geom, shape, transform):
    local_bounds = shapely.bounds(geom)
    if transform[4] < 0:  # if pixel_height is negative
        original_window = rasterio.windows.from_bounds(
            *local_bounds, transform=transform
        )
        gridded_window = rasterio.windows.round_window_to_full_blocks(
            original_window, [(1, 1)]
        )
        y_slice, x_slice = gridded_window.toslices()
        return x_slice, y_slice
    else:  # if pixel_height is not negative
        original_window = rasterio.windows.from_bounds(
            *local_bounds,
            transform=Affine(
                transform[0],
                transform[1],
                transform[2],
                transform[3],
                -transform[4],
                -transform[5],
            ),
        )
        gridded_window = rasterio.windows.round_window_to_full_blocks(
            original_window, [(1, 1)]
        )
        y_slice, x_slice = gridded_window.toslices()
        y_slice = slice(shape[0] - y_slice.stop, shape[0] - y_slice.start + 0)
        return x_slice, y_slice
