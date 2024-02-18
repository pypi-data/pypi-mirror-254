from typing import Optional

from fused.api import FusedAPI
from fused.quick.udf import run as _run
from fused.quick.udf import run_tile as _run_tile


def _detect_user_email():
    api = FusedAPI()
    return api._whoami()["email"]


def run_tile(
    email: str,
    id: Optional[str] = None,
    *,
    x: int,
    y: int,
    z: int,
    _client_id: Optional[str] = None,
    _dtype_out_vector: str = "parquet",
    _dtype_out_raster: str = "png",
    _include_log: bool = False,
    **params,
):
    if id is None:
        id = email
        email = _detect_user_email()

    res = _run_tile(
        x=x,
        y=y,
        z=z,
        udf_email=email,
        udf_id=id,
        data=params,
        client_id=_client_id,
        dtype_out_vector=_dtype_out_vector,
        dtype_out_raster=_dtype_out_raster,
    )
    if _include_log:
        return res
    else:
        return res.data


def run_file(
    email: str,
    id: Optional[str] = None,
    *,
    _client_id: Optional[str] = None,
    _dtype_out_vector: str = "parquet",
    _dtype_out_raster: str = "png",
    _include_log: bool = False,
    **params,
):
    if id is None:
        id = email
        email = _detect_user_email()

    res = _run(
        df_left=None,
        udf_email=email,
        udf_id=id,
        params=params,
        client_id=_client_id,
        dtype_out_vector=_dtype_out_vector,
        dtype_out_raster=_dtype_out_raster,
    )
    if _include_log:
        return res
    else:
        return res.data
