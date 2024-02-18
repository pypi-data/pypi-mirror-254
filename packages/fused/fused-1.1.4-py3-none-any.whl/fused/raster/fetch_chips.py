import asyncio
from io import BytesIO
from typing import Any, Coroutine, Dict, List, Sequence, Union

import httpx
import numpy as np
import requests
import shapely.geometry
from affine import Affine
from httpx import AsyncClient
from pydantic import BaseModel
from pyproj import CRS
from shapely.geometry.base import BaseGeometry

from fused._options import options as OPTIONS

RASTER_PROD_SERVER_URL = "https://01pzuom3v1.execute-api.us-west-2.amazonaws.com"
RASTER_PREVIEW_SERVER_URL = "https://enyg2tt3o2.execute-api.us-west-2.amazonaws.com"
RASTER_STAGING_SERVER_URL = "https://mwyvwpqm23.execute-api.us-west-2.amazonaws.com"
RASTER_SERVER_URL = RASTER_PROD_SERVER_URL
RASTER_SERVER_TIMEOUT_SECONDS = 30


class RasterChip(BaseModel):
    array: np.ma.MaskedArray
    """A masked array containing pixel data from the desired raster. The array has three dimensions, ordered (bands, rows, columns). The window fetched from the raster contains the input geometry expanded to the nearest whole pixel.
    """

    transform: Affine
    """An affine transformation matrix describing the pixel positions in world space in the local coordinate system.
    """

    crs: CRS
    """The coordinate system of the image
    """

    raster_url: str
    """The url of the raster image that this chip was derived from."""

    projected_geom: BaseGeometry
    """The input geometry reprojected into the image's local coordinate system."""

    class Config:
        arbitrary_types_allowed = True


class RasterChipRequest(BaseModel):
    geometry: Dict
    raster_url: str


class ZonalStatsRequest(RasterChipRequest):
    methods: Sequence[str]


def fetch_chips(
    geometries: Sequence[BaseGeometry],
    raster_urls: Sequence[str],
    headers: Dict[str, str],
) -> List[RasterChip]:
    return asyncio.run(
        _fetch_chips_async(
            geometries=geometries,
            raster_urls=raster_urls,
            headers=headers,
        )
    )


async def _fetch_chips_async(
    geometries: Sequence[BaseGeometry],
    raster_urls: Sequence[str],
    headers: Dict[str, str],
) -> List[RasterChip]:
    async with httpx.AsyncClient(timeout=RASTER_SERVER_TIMEOUT_SECONDS) as client:
        tasks: List[Coroutine[Any, Any, RasterChip]] = []
        for geometry, raster_url in zip(geometries, raster_urls):
            task = _fetch_chip_async(
                client=client,
                geometry=geometry,
                raster_url=raster_url,
                headers=headers,
            )
            tasks.append(task)

        return await asyncio.gather(*tasks)


def _parse_chip_response(buf: bytes, raster_url: str) -> RasterChip:
    with BytesIO(buf) as bio:
        file = np.load(bio)
        return RasterChip(
            array=np.ma.masked_array(file["data"], mask=file["mask"]),
            transform=Affine(*file["transform"]),
            crs=CRS.from_wkt(file["crs"].tobytes().decode("utf-8")),
            raster_url=raster_url,
            projected_geom=shapely.from_wkb(file["projected_geom"].tobytes()),
        )


async def _fetch_chip_async(
    *,
    client: AsyncClient,
    geometry: BaseGeometry,
    raster_url: str,
    headers: Dict[str, str],
):
    url = f"{RASTER_SERVER_URL}/v1/raster/sample_chip"
    data = RasterChipRequest(
        geometry=shapely.geometry.mapping(geometry),
        raster_url=raster_url,
    ).dict()

    r = await client.post(url, json=data, headers=headers)

    # We had issues with follow_redirects resulting in 403 from S3,
    # so we manually follow redirects
    if r.status_code == 303:
        redirect_url = r.headers["Location"]
        r = await client.get(redirect_url)

    r.raise_for_status()
    return _parse_chip_response(r.content, raster_url)


def _fetch_chip_sync(
    *,
    geometry: BaseGeometry,
    raster_url: str,
    headers: Dict[str, str],
):
    url = f"{RASTER_SERVER_URL}/v1/raster/sample_chip"
    data = RasterChipRequest(
        geometry=shapely.geometry.mapping(geometry),
        raster_url=raster_url,
    ).dict()

    r = requests.post(
        url,
        json=data,
        headers=headers,
        allow_redirects=True,
        timeout=OPTIONS.request_timeout,
    )
    r.raise_for_status()
    return _parse_chip_response(r.content, raster_url)


def fetch_zonal_stats(
    geometries: Sequence[BaseGeometry],
    raster_urls: Sequence[str],
    methods: Sequence[str],
    headers: Dict[str, str],
) -> List[Dict[str, Union[int, float, bool]]]:
    return asyncio.run(
        _fetch_zonal_stats_async(
            geometries=geometries,
            raster_urls=raster_urls,
            methods=methods,
            headers=headers,
        )
    )


async def _fetch_zonal_stats_async(
    geometries: Sequence[BaseGeometry],
    raster_urls: Sequence[str],
    methods: Sequence[str],
    headers: Dict[str, str],
) -> List[Dict[str, Union[int, float, bool]]]:
    async with httpx.AsyncClient(timeout=RASTER_SERVER_TIMEOUT_SECONDS) as client:
        tasks: List[Coroutine[Any, Any, Dict[str, Union[int, float, bool]]]] = []
        for geometry, raster_url in zip(geometries, raster_urls):
            task = _fetch_zonal_stats(
                client=client,
                geometry=geometry,
                raster_url=raster_url,
                methods=methods,
                headers=headers,
            )
            tasks.append(task)

        return await asyncio.gather(*tasks)


def _parse_zonal_stats_response(body: Dict, raster_url: str) -> Dict[str, Any]:
    return {
        "raster_url": raster_url,
        **body,
    }


async def _fetch_zonal_stats(
    *,
    client: AsyncClient,
    geometry: BaseGeometry,
    raster_url: str,
    methods: Sequence[str],
    headers: Dict[str, str],
):
    url = f"{RASTER_SERVER_URL}/v1/raster/zonal_stats"
    data = ZonalStatsRequest(
        geometry=shapely.geometry.mapping(geometry),
        raster_url=raster_url,
        methods=methods,
    ).dict()

    r = await client.post(url, json=data, headers=headers)
    r.raise_for_status()
    return _parse_zonal_stats_response(r.json(), raster_url)


def _set_raster_base_url(base_url: str):
    global RASTER_SERVER_URL
    RASTER_SERVER_URL = base_url
