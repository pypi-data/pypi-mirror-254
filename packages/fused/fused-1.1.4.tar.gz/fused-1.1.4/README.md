<h1 align="center">
  Fused Public Python package
</h1>
<h3 align="center">
  🌎 Code to Map. Instantly.
</h3>
<br><br>

![version](https://img.shields.io/badge/version-1.1.2-blue)

**Fused** is a Python library to code, scale, and ship geospatial workflows of any size. Express workflows as shareable UDFs (user defined functions) without thinking about the underlying compute. The Fused Python library is maintained by [Fused.io](https://fused.io).

## Prerequisites

Python >= 3.8

## Install

Fused is currently in private beta. Email info@fused.io for access.

```
pip install fused
```

## Quickstart

```python3
import fused


# Load data
census = 's3://fused-asset/infra/census_bg_us/'
buildings = 's3://fused-asset/infra/building_msft_us/'

# Declare UDF
@fused.udf()
def census_buildings_join(left, right):
    import fused
    df_joined = fused.utils.geo_join(left.data, right.data)
    df_cnt = df_joined.groupby(['fused_index','GEOID']).size().to_frame('count_building').reset_index()
    return df_cnt

# Instantiate job configuration that runs the data against the UDF
job = census_buildings_join(census, buildings)

# Run locally
job.run_local()

# Run on remote compute managed by Fused and view logs
job_id = job.run_remote(output_table='s3://my-s3-bucket/census_buildings_join')
job_id.tail_logs()

# Export job to local directory
job.export('census_buildings_join', overwrite=True)

# Re-import job
fused.load_job('census_buildings_join')
```


## Available operations
The following are some of the key functions:

- [ingest](https://www.fused.io/api/top-level-functions/?h=ingest#fused.ingest): Upload a dataset into S3 with the Fused format.
- [open_table](https://www.fused.io/api/top-level-functions/?h=run_local#fused.open_table): Open a Table object given a path to the root of the table
- [run_local](https://www.fused.io/api/udf/?h=run_local#fused.models.udf.udf.GeoPandasUdfV2.run_local): Execute data processing tasks locally while you test and debug.
- [run_remote](https://www.fused.io/api/job/?h=run_remote#fused.models.api.job.JobStepConfig.run_remote): Submit jobs to run on a remote clusters - by changing a single line of code.
- export: Save a job and its configuration as a local directory, zip file, or gist.
- [load_job](https://www.fused.io/api/top-level-functions/?h=run_local#fused.load_job): Open a previously saved job.
- [load_udf](https://www.fused.io/api/top-level-functions/?h=run_local#fused.load_udf): Open a previously saved UDF.
- [show](https://www.fused.io/api/job/?h=show#fused.models.api.job.JoinJobStepConfig.show): Debugger tool.
- render: Render job or UDF to new Notebook cell and edit.

See the [Fused documentation](https://docs.fused.io/) for the full list of available functions.

## Docs
The documentation is a work in progress. It follows the Diátaxis system:

- Getting Started Tutorial: A hands-on introduction to Fused.
- [How-to guides](https://www.fused.io/use_cases/cmip6/): Simple step-by-step user guides to accomplish specific tasks.
- [Reference guide](https://www.fused.io/api/top-level-functions/): Commands, modules, classes and methods.
- [Explanation](https://www.fused.io/): Discussion of key decisions and design philosophy of the library.

## Changelog
See the [changelog](https://docs.fused.io/fused_py/changelog/) for the latest changes.
