from typing import Optional, Union

import geopandas as gpd

from fused._public_api import open_table


def get_chunks_metadata(url: str) -> gpd.GeoDataFrame:
    """Returns a GeoDataFrame with each chunk in the table as a row.

    Args:
        url: URL of the table.
    """
    t = open_table(url, fetch_samples=False)
    return t.metadata_gdf


def get_chunk_from_table(
    url: str, file_id: Union[str, int, None], chunk_id: Optional[int]
) -> gpd.GeoDataFrame:
    """Returns a chunk from a table and chunk coordinates.

    This can be called with file_id and chunk_id from `get_chunks_metadata`.

    Args:
        url: URL of the table.
        file_id: File ID to read.
        chunk_id: Chunk ID to read.
    """
    # TODO: may want to cache this open_table call
    t = open_table(url, fetch_samples=False)
    return t.get_chunk(file_id, chunk_id)
