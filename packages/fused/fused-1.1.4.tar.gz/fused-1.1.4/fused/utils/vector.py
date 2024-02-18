from typing import Sequence

import geopandas as gpd
import pandas as pd

from fused.models.udf.common import Chunk, Chunks


def sjoin(
    left: Chunk,
    right: Chunks,
    *,
    right_cols: Sequence[str] = (),
    left_cols: Sequence[str] = ("fused_index", "fused_area", "geometry"),
) -> gpd.GeoDataFrame:
    """Helper to run a geopandas sjoin on a join sample

    Args:
        left: a sample on which to run `sjoin`.
        right: samples on which to run `sjoin`.
        right_cols: The columns of the right input to keep.
        left_cols: The columns of the left input to keep. Defaults to ("fused_index", "fused_area", "geometry").

    Returns:
        The spatially joined data.
    """
    # Pandas needs a list of strings as input
    left_cols = list(left_cols)
    right_cols = list(right_cols)

    if len(right_cols) == 0:
        msg = (
            "`right_cols` must be provided. "
            f"The columns in the right dataset are: {right[0].data.columns}"
        )
        raise TypeError(msg)

    left_data = left.data
    assert isinstance(left_data, gpd.GeoDataFrame)
    if not left_cols:
        left_cols = list(left_data.columns)

    right_table = pd.concat([i.data for i in right])

    assert (
        left_data._geometry_column_name in left_cols
    ), "geometry column not included in left_cols"

    assert (
        right_table._geometry_column_name in right_cols
    ), "geometry column not included in right_cols"

    # The only column that overlaps between the two datasets should be the geometry
    # column
    assert (
        set(left_cols).difference({"geometry"}).isdisjoint(right_cols)
    ), "Left and right columns must not overlap."

    assert (
        len(set(left_cols).difference(left_data.columns)) == 0
    ), "All left columns must exist in the left DataFrame."

    assert (
        len(set(right_cols).difference(right_table.columns)) == 0
    ), "All left columns must exist in the right DataFrame."

    return left_data[left_cols].sjoin(right_table[right_cols])
