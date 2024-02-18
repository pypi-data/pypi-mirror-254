from typing import Dict, Tuple

import numpy as np
from affine import Affine
from numpy.typing import NDArray


def rasterize_geometry(
    geom: Dict, shape: Tuple[int, int], affine: Affine, all_touched: bool = False
) -> NDArray[np.uint8]:
    """Return an image array with input geometries burned in.

    Args:
        geom: GeoJSON geometry
        shape: desired 2-d shape
        affine: transform for the image
        all_touched: rasterization strategy. Defaults to False.

    Returns:
        numpy array with input geometries burned in.
    """

    from rasterio import features

    geoms = [(geom, 1)]
    rv_array = features.rasterize(
        geoms,
        out_shape=shape,
        transform=affine,
        fill=0,
        dtype="uint8",
        all_touched=all_touched,
    )

    return rv_array.astype(bool)
