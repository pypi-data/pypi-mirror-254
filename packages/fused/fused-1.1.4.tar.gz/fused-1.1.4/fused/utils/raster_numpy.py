from __future__ import annotations

import json
import warnings
from concurrent.futures import Future, ThreadPoolExecutor
from io import BytesIO
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
)
from zipfile import ZipFile

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
from affine import Affine
from shapely.geometry.base import BaseGeometry

from fused._global_api import get_api
from fused._options import options as OPTIONS
from fused.types import ChipResponse

if TYPE_CHECKING:
    from fused.api.api import FusedAPI


def fetch_chip(
    fused_index: int,
    geometry: BaseGeometry,
    href: str,
    *,
    asset_name: Optional[str] = None,
    datetime=None,
    api: Optional[FusedAPI] = None,
) -> ChipResponse:
    """Fetch a single raster chip given a geometry and GeoTIFF

    Args:
        fused_index: An integer derived from the `fused_index` column in the sample data.
        geometry: A Shapely geometry instance, in the same coordinate system as the GeoTIFF image.
        href: The url to a GeoTIFF to load.

    Keyword Args:
        asset_name: The name of the asset. This is returned  Defaults to None.
        datetime: The date time and which . Defaults to None.
        api: An instance of FusedAPI. Defaults to None, in which case it uses the global API.

    Returns:
        A dictionary with a single chip of data.
    """
    if not api:
        api = get_api()

    return api._fetch_row(
        fused_index=fused_index,
        geometry=geometry,
        href=href,
        asset_name=asset_name,
        datetime=datetime,
    )


def get_raster_numpy(
    left,
    right,
    *,
    asset_names: Sequence[str],
    n_rows: Optional[int] = None,
    prefetch_entire_files: bool = False,
    buffer: Optional[float] = None,
    href_modifier: Optional[Callable[[str], str]] = None,
    href_mapping: Optional[Dict[str, str]] = None,
    additional_columns: Optional[Sequence[str]] = None,
    context: None = None,
    api: Optional[FusedAPI] = None,
    load_chips: bool = True,
    serialize_outputs: bool = False,
    write_sidecar_zip: bool = False,
    output=None,
    _fetch_all_at_once: bool = False,
    **kwargs,
) -> Iterator[Dict[str, Any]]:
    """Get a raster as a numpy array

    Args:
        left: The input join object with geometries.
        right: The input join object with STAC data.

    Keyword Args:
        asset_names: The name(s) of assets in the STAC data to use.
        n_rows: A limit to the number of rows used from the left side. Defaults to None.
        prefetch_entire_files: If True, on the backend will fetch entire files to the local machine instead of doing partial reads from S3. Defaults to False.
        buffer: If set, will buffer the data by this amount (in meters) before fetching the raster data. Note that this buffer happens after the join between left and right. Defaults to None.
        href_modifier: A function to modify asset hrefs before fetching. Defaults to None.
        href_mapping: A dictionary from `str` to `str` that specifies how to change asset hrefs before fetching data. Note that `href_modifier` is applied after `href_mapping`. Defaults to None.
        additional_columns: Additional column names from the input DataFrame to add onto the raster results. Defaults to None.
        context: Unused in the local `fused` version. On the server this has context information. Defaults to None.
        api: An instance of `FusedAPI` to use for interacting with the backend. Defaults to None.
        load_chips: If False, will not fetch any data. Defaults to True.
        serialize_outputs: If True, will include `crs`, `transform`, `datetime`, `projected_geom`, and `shape` onto each row. Defaults to False.
        write_sidecar_zip: This is used for writing chips to sidecar, but only on the server side. Defaults to False.
        output: This is used for writing chips to sidecar, but only on the server side. Defaults to None.
        _fetch_all_at_once: If True, will parallelize downloads. Defaults to False.

    Yields:
        A dictionary of records with each row's information.
    """
    # write_sidecar_zip is unused here
    # context is unused here
    # prefetch_entire_files is unused here
    if type(prefetch_entire_files) != bool:
        warnings.warn("prefetch_entire_files has an invalid type (not bool)")

    if write_sidecar_zip and output is None:
        raise TypeError("Pass `output=output` when using write_sidecar_zip")

    left_gdf = left.data[:n_rows]
    right_gdf = right.data
    df = gpd.sjoin(left_gdf, right_gdf.drop(columns=["fused_index"]))

    if not asset_names:
        # TODO: Do we want to sniff the asset names or not?
        if not len(df):
            return
        row0 = df.iloc[0]
        asset_names = row0["assets"].keys()

    if href_mapping:
        orig_href_modifier = href_modifier

        def _href_mapping_modifier(url: str) -> str:
            url = href_mapping.get(url, url)
            return orig_href_modifier(url) if orig_href_modifier is not None else url

        href_modifier = _href_mapping_modifier

    if buffer:
        df = df.copy()
        df.geometry = df.geometry.buffer(buffer)

    def _get_single_row(*, asset_name: str, row: pd.Series) -> Dict:
        datetime = None
        if "datetime" in row:
            datetime = row["datetime"]

        href = row["assets"][asset_name]["href"]
        if href_modifier:
            href = href_modifier(href)

        fetch_chip_results = fetch_chip(
            fused_index=row["fused_index"],
            geometry=row["geometry"],
            href=href,
            asset_name=asset_name,
            datetime=datetime,
            api=api,
        )

        additional_kws = {}
        if additional_columns:
            for col in additional_columns:
                # If the name is provided by fetch_chip,
                # we won't find it on the original row anyways
                if col not in fetch_chip_results:
                    additional_kws[col] = row[col]

        result = {
            **additional_kws,
            **fetch_chip_results,
        }

        # TODO: We do not actually write the chips locally
        result["chip_path"] = "sample value (will be a file path when run)"

        if serialize_outputs:
            # TODO: We do not actually write the chips locally
            # result["chip_path"] = str(result["chip_path"])
            result["crs"] = str(result["crs"])
            result["transform"] = json.dumps(result["transform"])
            result["datetime"] = str(result["datetime"])
            result["projected_geom"] = shapely.to_wkb(result["projected_geom"])
            result["shape"] = json.dumps(result["shape"])

        if not load_chips:
            # This is a fix-up to match what the backend will do
            result.pop("array_data")
            result.pop("array_mask")

        return result

    if _fetch_all_at_once:
        with ThreadPoolExecutor(max_workers=OPTIONS.max_workers) as pool:
            futures: List[Future] = []
            for asset_name in asset_names:
                for _, row in df.iterrows():
                    futures.append(
                        pool.submit(_get_single_row, asset_name=asset_name, row=row)
                    )
            for future in futures:
                yield future.result()
    else:
        for asset_name in asset_names:
            for _, row in df.iterrows():
                result = _get_single_row(asset_name=asset_name, row=row)
                yield result


def get_raster_numpy_grouped(
    left,
    right,
    *,
    group_by: Sequence[str],
    asset_names: Sequence[str],
    n_rows: Optional[int] = None,
    prefetch_entire_files: bool = False,
    buffer: Optional[float] = None,
    href_modifier: Optional[Callable[[str], str]] = None,
    href_mapping: Optional[Dict[str, str]] = None,
    context: None = None,
    api: Optional[FusedAPI] = None,
    load_chips: bool = True,
    serialize_outputs: bool = False,
    write_sidecar_zip: bool = False,
    output=None,
    _fetch_all_at_once: bool = True,
    **kwargs,
) -> Iterable[pd.DataFrame]:
    """Fetch rasters and then group by columns

    Args:
        left: The input join object with geometries.
        right: The input join object with STAC data.

    Keyword Args:
        group_by: The column(s) to group on.
        asset_names: The name(s) of assets in the STAC data to use.
        n_rows: A limit to the number of rows used from the left side. Defaults to None.
        prefetch_entire_files: If True, on the backend will fetch entire files to the local machine instead of doing partial reads from S3. Defaults to False.
        buffer: If set, will buffer the data by this amount (in meters) before fetching the raster data. Note that this buffer happens after the join between left and right. Defaults to None.
        href_modifier: A function to modify asset hrefs before fetching. Defaults to None.
        href_mapping: A dictionary from `str` to `str` that specifies how to change asset hrefs before fetching data. Note that `href_modifier` is applied after `href_mapping`. Defaults to None.
        additional_columns: Additional column names from the input DataFrame to add onto the raster results. Defaults to None.
        context: Unused in the local `fused` version. On the server this has context information. Defaults to None.
        api: An instance of `FusedAPI` to use for interacting with the backend. Defaults to None.
        load_chips: If False, will not fetch any data. Defaults to True.
        serialize_outputs: If True, will include `crs`, `transform`, `datetime`, `projected_geom`, and `shape` onto each row. Defaults to False.
        write_sidecar_zip: This is used for writing chips to sidecar, but only on the server side. Defaults to False.
        output: This is used for writing chips to sidecar, but only on the server side. Defaults to None.
        _fetch_all_at_once: If True, will parallelize downloads. Defaults to False.

    Yields:
        DataFrames with raster values per group of `group_by` columns
    """
    records = list(
        get_raster_numpy(
            left=left,
            right=right,
            asset_names=asset_names,
            n_rows=n_rows,
            prefetch_entire_files=prefetch_entire_files,
            buffer=buffer,
            href_modifier=href_modifier,
            href_mapping=href_mapping,
            additional_columns=group_by,
            context=context,
            api=api,
            load_chips=load_chips,
            serialize_outputs=serialize_outputs,
            write_sidecar_zip=write_sidecar_zip,
            output=output,
            _fetch_all_at_once=_fetch_all_at_once,
            **kwargs,
        )
    )
    out_df = pd.DataFrame.from_records(records)
    # Spread into list as group_by may not be a tuple
    groups = out_df.groupby([*group_by], group_keys=True)
    for group in groups:
        # Return the first group's DataFrame (not the ID in group[0])
        yield group[1]


def get_raster_numpy_from_chips(
    input, sidecar_table_name: str, n_rows: Optional[int] = None, **kwargs
):
    """Get numpy array from chips

    Args:
        input: The input join object with left being geometries and right being STAC data.
        sidecar_table_name: The name of the table in `input` that contains chips as its sidecar file.
        n_rows: The number of chips to load from the sidecar. Defaults to None, which loads all chips.

    Yields:
        Dictionaries that contain chip data.
    """
    # input.data is copied so that we don't permanently modify the types,
    # and this function can be run on the same sample again
    df = input.data.copy()
    df["shape"] = df["shape"].map(json.loads)
    df["projected_geom"] = df["projected_geom"].map(shapely.from_wkb)

    def _load_transform(x: Optional[str]) -> Affine:
        if not x:
            return None
        obj = json.loads(x)
        if not obj:
            return None
        return Affine(*obj)

    df["transform"] = df["transform"].map(_load_transform)

    with BytesIO(input.sidecar[sidecar_table_name]) as bio:
        with ZipFile(bio, mode="r") as zf:
            len_rows = len(df)
            if n_rows is not None:
                len_rows = min(n_rows, len_rows)
            for i in range(len_rows):
                row = df.iloc[i].copy()
                if row["chip_path"]:
                    with zf.open(row["chip_path"], mode="r") as zfio:
                        npz_data = np.load(zfio)
                        row["array_data"] = npz_data["data"]
                        row["array_mask"] = npz_data["mask"]

                        yield row.to_dict()
