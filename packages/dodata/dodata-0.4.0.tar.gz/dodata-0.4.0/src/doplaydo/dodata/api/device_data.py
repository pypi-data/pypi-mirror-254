"""Common API calls to device_data namespace."""
from __future__ import annotations
import json
import pandas as pd
from pathlib import Path
from typing import Literal, TypeAlias
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from tqdm.auto import tqdm

import pydantic
import requests

from .common import url as base_url, get, post
from .api_types import Attributes
from .. import settings

JSONDict: TypeAlias = "dict[str, int | float | str | JSONDict]"


class PlottingKwargs(pydantic.BaseModel):
    """Model for plotting kwargs."""

    x_col: str
    y_col: str | list[str]
    x_name: str
    y_name: str
    x_units: str | None = None
    y_units: str | None = None
    grouping: dict[str, int] | None = pydantic.Field(default_factory=dict)
    sort_by: dict[str, bool] | None = pydantic.Field(default_factory=dict)
    x_log_axis: bool = False
    y_log_axis: bool = False
    x_limits: tuple[float, float] | None = None
    y_limits: tuple[float, float] | None = None
    scatter: bool = False


def upload(
    file: str | Path | tuple[str, bytes],
    project_id: str,
    device_id: str,
    data_type: Literal["simulation", "measurement"] = "measurement",
    attributes: Attributes | None = None,
    plotting_kwargs: PlottingKwargs | None = None,
    wafer_id: str | None = None,
    die_x: int | None = None,
    die_y: int | None = None,
) -> requests.Response:
    """Upload a new project to DoData.

    Args:
        file: Path to the file to upload.
        project_id: Name of the project to upload to.
        device_id: Name of the device to upload to.
        data_type: Type of data to upload. Either "simulation" or "measurement".
        attributes: attributes data to upload with the file.
        plotting_kwargs: Plotting kwargs to upload with the file.
        wafer_id: Name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.

    """
    url = f"{base_url}/device_data/"
    attributes = attributes or {}

    params: dict[str, str | int] = {
        "project_id": project_id,
        "device_id": device_id,
        "data_type": data_type,
    }
    data: JSONDict = {}

    if attributes:
        data["attributes"] = json.dumps(attributes)
    if plotting_kwargs:
        data["plotting_kwargs"] = json.dumps(plotting_kwargs.model_dump())
    if wafer_id is not None:
        params["wafer_id"] = wafer_id
    if die_x is not None:
        params["die_x"] = die_x
    if die_y is not None:
        params["die_y"] = die_y

    if isinstance(file, tuple):
        response = post(url, params=params, files={"data_file": file}, data=data)
    else:
        fp = Path(file).expanduser().resolve()
        assert (
            fp.exists() and fp.is_file()
        ), f"{fp.resolve()} doesn't exists or is not a file"
        with open(fp, "rb") as f:
            response = post(url, params=params, files={"data_file": f}, data=data)

    if response.status_code != 200:
        raise requests.HTTPError(
            f"{response.text}, {wafer_id=}, {die_x=}, {die_y=}, {project_id=},"
            f" {device_id=}, {data_type=}",
            response=response,
        )
    return response


def upload_multi(
    files: list[str | Path | tuple[str, bytes]],
    project_ids: list[str],
    device_ids: list[str],
    data_types: list[Literal["simulation", "measurement"]],
    attributes: list[dict[str, str | int | float]] | None = None,
    plotting_kwargs: list[PlottingKwargs | None] | None = None,
    wafer_ids: list[str | None] | None = None,
    die_xs: list[int | None] | None = None,
    die_ys: list[int | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> None:
    """Upload multiple files in parallel.

    The upload is handled with a ThreadPoolExecutor.

    All args/kwargs must have the same length as `files` unless they can be `None`.

    Args:
        files: List of files to upload.
        project_ids: List of project names to upload to.
        device_ids: List of device names to upload to.
        data_types: List of data types to upload. Either "simulation" or "measurement".
        attributes: List of attributes data to upload with the files.
        plotting_kwargs: List of plotting kwargs to upload with the files.
        wafer_ids: List of wafer names to upload to.
        die_xs: List of X coordinates of the dies to upload to.
        die_ys: List of Y coordinates of the dies to upload to.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for i, file in enumerate(files):
            project_id = project_ids[i]
            device_id = device_ids[i]
            data_type = data_types[i]
            if attributes is not None:
                attrs = attributes[i]
            else:
                attrs = None
            if plotting_kwargs is not None:
                plt_kwargs = plotting_kwargs[i]
            else:
                plt_kwargs = None
            if wafer_ids is not None:
                wafer_id = wafer_ids[i]
            else:
                wafer_id = None
            if die_xs is not None:
                die_x = die_xs[i]
            else:
                die_x = None
            if die_ys is not None:
                die_y = die_ys[i]
            else:
                die_y = None

            futures.append(
                e.submit(
                    upload,
                    file=file,
                    project_id=project_id,
                    device_id=device_id,
                    data_type=data_type,
                    attributes=attrs,
                    plotting_kwargs=plt_kwargs,
                    wafer_id=wafer_id,
                    die_x=die_x,
                    die_y=die_y,
                )
            )
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)


@pydantic.validate_call
def download(
    project_id: str,
    cell_id: str | None = None,
    device_id: str | None = None,
    wafer_id: str | None = None,
    die_x: int | None = None,
    die_y: int | None = None,
    data_type: Literal["simulation", "measurement"] = "measurement",
) -> requests.Response:
    """Download data DoData.

    Args:
        project_id: Name of the project to download.
        cell_id: Name of the cell to download.
        device_id: Name of the device to download.
        wafer_id: Name of the wafer to download.
        die_x: X coordinate of the die to download.
        die_y: Y coordinate of the die to download.
        data_type: Type of data to download. Either "simulation" or "measurement".

    """
    url = f"{base_url}/device_data/{project_id}/data_files"

    params: dict[str, str | int] = {}
    if cell_id:
        params["cell_id"] = cell_id
    if device_id:
        params["device_id"] = device_id
    if wafer_id:
        params["wafer_id"] = wafer_id
    if die_x is not None:
        params["die_x"] = die_x
    if die_y is not None:
        params["die_y"] = die_y
    if data_type:
        params["data_type"] = data_type

    return get(url=url, params=params)


def get_data_by_pkey(device_data_pkey: int) -> pd.DataFrame:
    """Retrieve device data by its unique identifier and return it as a DataFrame.

    Args:
        device_data_pkey (int): Serial primary key representing a device data record.

    Raises:
        HTTPException: If the HTTP request to the endpoint fails.

    Returns:
        pd.DataFrame | None: A pandas DataFrame containing the raw data of the
            specified device data record, or None if the request was unsuccessful.

    Example:
        import dodata_sdk as ddk
        ddk.get_data_by_pkey(123)
    """
    response = get(f"{base_url}/device_data/{device_data_pkey}/raw_data")
    if response.status_code != 200:
        requests.HTTPError(response.text, response=response)
    return pd.DataFrame(response.json())
