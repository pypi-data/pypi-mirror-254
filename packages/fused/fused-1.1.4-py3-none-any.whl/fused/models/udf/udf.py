from __future__ import annotations

from contextlib import ExitStack
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Optional, Sequence, TextIO, Union

from pydantic import Field, PrivateAttr

from fused.models.schema import Schema
from fused.models.udf._eval_result import UdfEvaluationResult
from fused.models.udf.base_udf import BaseUdf

from .._inplace import _maybe_inplace

if TYPE_CHECKING:
    from fused.models.input import BaseInput


class JoinType(str, Enum):
    LEFT = "left"
    INNER = "inner"


class UdfType(str, Enum):
    GEOPANDAS_V2 = "geopandas_v2"


class GeoPandasUdfV2(BaseUdf, type=UdfType.GEOPANDAS_V2):
    """A user-defined function that operates on [`geopandas.GeoDataFrame`s][geopandas.GeoDataFrame]."""

    type: UdfType = UdfType.GEOPANDAS_V2
    table_schema: Optional[Schema] = None
    """The [`Schema`][fused.models.Schema] describing the output of this UDF.
    """

    entrypoint: str
    """Name of the function within the code to invoke."""

    parameters: Dict[str, Any] = Field(default_factory=dict)
    """Parameters to pass into the entrypoint."""

    _parameter_list: Optional[Sequence[str]] = PrivateAttr(None)
    original_headers: Optional[str] = None

    def set_parameters(
        self,
        parameters: Dict[str, Any],
        replace_parameters: bool = False,
        inplace: bool = False,
    ) -> "GeoPandasUdfV2":
        """Set the parameters on this UDF.

        Args:
            parameters: The new parameters dictionary.
            replace_parameters: If True, unset any parameters not in the parameters argument. Defaults to False.
            inplace: If True, modify this object. If False, return a new object. Defaults to True.
        """
        ret = _maybe_inplace(self, inplace)
        new_parameters = (
            parameters
            if replace_parameters
            else {
                **ret.parameters,
                **parameters,
            }
        )
        ret.parameters = new_parameters
        return ret

    def to_file(self, where: Union[str, Path, TextIO]):
        """Write the UDF to disk or the specified file-like object.

        Args:
            where: A path to a file or a file-like object.
        """
        with ExitStack() as ctx:
            if isinstance(where, str) or isinstance(where, Path):
                where = ctx.enter_context(open(where, "w"))

            where.write(self.code)

    def eval_schema(self, inplace: bool = False) -> "GeoPandasUdfV2":
        """Reload the schema saved in the code of the UDF.

        Note that this will evaluate the UDF function.

        Args:
            inplace: If True, update this UDF object. Otherwise return a new UDF object (default).
        """
        from fused._udf.execute_v2 import execute_for_decorator

        new_udf = execute_for_decorator(self)
        assert isinstance(
            new_udf, GeoPandasUdfV2
        ), f"UDF has unexpected type: {type(new_udf)}"
        ret = _maybe_inplace(self, inplace)
        ret.table_schema = new_udf.table_schema
        ret._parameter_list = new_udf._parameter_list
        return ret

    def run_local(
        self, sample: BaseInput, inplace: bool = False, **kwargs
    ) -> UdfEvaluationResult:
        """Evaluate this UDF against a sample.

        Args:
            sample: Sample (from `get_sample`) to execute against.
            inplace: If True, update this UDF object with schema information. (default)
        """
        from fused._udf.execute_v2 import execute_against_sample

        ret = _maybe_inplace(self, inplace)
        return execute_against_sample(udf=ret, input=sample, **kwargs)


EMPTY_UDF = GeoPandasUdfV2(
    name="EMPTY_UDF", code="", entrypoint="", table_schema=Schema(fields=[])
)
