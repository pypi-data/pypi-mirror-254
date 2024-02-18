import sys
import warnings
from typing import Optional, Union

from fused._global_api import get_api
from fused._udf import coerce_to_udf
from fused.models import (
    JobStepConfig,
    JoinJobStepConfig,
    JoinSinglefileJobStepConfig,
    MapJobStepConfig,
    UdfJobStepConfig,
)
from fused.models.api.dataset import JobMetadata, Table
from fused.models.udf import BaseUdf
from fused.warnings import FusedDefaultWarning


def explain_udf(
    udf: Union[
        BaseUdf,
        dict,
        MapJobStepConfig,
        JoinJobStepConfig,
        JoinSinglefileJobStepConfig,
        UdfJobStepConfig,
        JobMetadata,
        Table,
    ],
) -> str:
    """Explain the UDF.

    Args:
        udf: The UDF to explain.

    Returns:
        AI generated explanation of the UDF.
    """
    # TODO: Accept the job step config?
    api = get_api()

    op = None
    if isinstance(udf, Table):
        op = udf.parent.job.type
    elif isinstance(udf, JobMetadata):
        op = udf.job.type
    elif isinstance(udf, JobStepConfig):
        op = udf.type

    udf = coerce_to_udf(udf)

    return api._explain_udf(udf, operation=op)


def debug_udf(
    udf: Union[
        BaseUdf,
        dict,
        MapJobStepConfig,
        JoinJobStepConfig,
        JoinSinglefileJobStepConfig,
        JobMetadata,
        Table,
        None,
    ] = None,
    error: Optional[str] = None,
    job_id: Optional[str] = None,
) -> str:
    """Explain the UDF error.

    Args:
        udf: The UDF to explain. If not set, the last UDF run in a Fused magic cell is used.
        error: The error message from the job. If using the last UDF run, this defaults to the error from the last run.
        job_id: The job to retrieve an error message from.

    Returns:
        AI generated explanation of the UDF error.
    """
    api = get_api()

    if job_id:
        assert error is None
        # Retrieve the last message from the job, which is probably where the error is printed
        error = api.get_logs(job_id)[-1]["message"]

    if error is None:
        error = f"{sys.last_value}" if sys.last_value is not None else None
        if error is not None:
            warnings.warn(f"Detected the last error as: {error}", FusedDefaultWarning)

    assert (
        error is not None or job_id is not None
    ), "job_id must be specified if an error message is not passed"

    udf = coerce_to_udf(udf)

    return api._debug_udf(udf=udf, error=error)
