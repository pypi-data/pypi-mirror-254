import asyncio
from typing import Callable, Dict, Literal, Optional, Sequence

import pandas as pd

from fused.api import FusedAPI
from fused.utils import sjoin

ZonalStatsMethod = Literal["max", "min", "sum", "mean", "count"]
"""Aggregation method for [zonal_stats][fused.quick.zonal_stats.zonal_stats]."""


def zonal_stats(
    left,
    right,
    *,
    n_rows: Optional[int] = None,
    left_cols: Sequence[str] = ("fused_index", "fused_area", "geometry"),
    right_cols: Sequence[str] = ("assets", "geometry", "datetime"),
    sort_by_col: Optional[str] = "fused_area",
    asset_mapper: Callable[[Dict], str] = lambda asset: asset["naip-analytic"]["href"],
    methods: Sequence[ZonalStatsMethod] = ("sum", "mean", "max", "min", "count"),
    api: Optional[FusedAPI] = None,
) -> pd.DataFrame:
    """Run interactive zonal statistics on a join sample

    Args:
        left: a sample of geometries to run zonal statistics on.
        right: a sample of STAC to run zonal statistics on.
        n_rows: The number of rows to select for running zonal statistics. Defaults to None, in which case all rows will be used.
        left_cols: The column names of the left input to keep. Defaults to ("fused_index", "fused_area", "geometry").
        right_cols: The column names of the right input to keep. Defaults to ("assets", "geometry", "datetime").
        sort_by_col: The column on which to sort before running zonal stats. Defaults to "fused_area".
        asset_mapper: A function to select the `href` from the STAC asset column. Defaults to `lambda asset:asset["naip-analytic"]["href"]`.
        methods: The zonal statistics methods to use. Defaults to ("sum", "mean", "max", "min", "count").
        api: A FusedAPI instance. Defaults to None, in which case a FusedAPI instance will be constructed from saved credentials.

    Examples:

        ```py
        left = api.open_table("s3://...")
        right = api.open_table("s3://...")
        input = left.join(right).get_sample()
        df_zonal_stats = utils.zonal_stats(
            input.left,
            input.right,
            left_cols=["fused_index", "fused_area", "geometry"],
            n_rows=10,
            asset_mapper=lambda asset: asset["naip-analytic"]["href"],
        )
        ```

    Returns:
        `DataFrame` with zonal statistics.
    """
    # Note: this _should_ work as long as credentials have been saved to a file
    if not api:
        api = FusedAPI()

    # If there's already a running event loop, import `nest_asyncio` to allow event loop
    # nesting
    try:
        asyncio.get_running_loop()

        import nest_asyncio

        nest_asyncio.apply()
    except RuntimeError:
        pass

    joined_data = sjoin(left, right, right_cols=right_cols, left_cols=left_cols)

    if sort_by_col is not None:
        joined_data = joined_data.sort_values(sort_by_col)

    joined_data["raster_url"] = joined_data["assets"].map(asset_mapper)

    if n_rows:
        joined_data = joined_data.iloc[:n_rows]

    stats = asyncio.run(
        api._zonal_stats(
            joined_data["geometry"].to_list(),
            joined_data["raster_url"].to_list(),
            methods=methods,
        )
    )
    stats_df = pd.DataFrame(stats)
    joined_data[stats_df.columns] = stats_df.values
    return joined_data
