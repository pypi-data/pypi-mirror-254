from typing import Any, List, Optional, TypedDict

from affine import Affine
from numpy.typing import NDArray
from pyproj import CRS
from shapely.geometry.base import BaseGeometry


class ChipResponse(TypedDict):
    fused_index: int
    datetime: Any
    array_data: NDArray
    array_mask: NDArray
    crs: CRS
    transform: Affine
    filepath: str
    asset_name: Optional[str]
    projected_geom: BaseGeometry
    shape: List[int]
