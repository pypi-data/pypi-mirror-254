"""Common API calls to device_data namespace."""
from __future__ import annotations
import json
from tqdm.auto import tqdm

import requests

from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from io import BytesIO
from PIL import Image
from .common import url as base_url, post, get
from .. import settings
from ..db.analysis import (
    get_analyses_for_die,
    get_analyses_for_wafer,
    get_analyses_for_device_data,
)
from doplaydo.dodata_core.models import Analysis
from collections.abc import Sequence
from typing import Literal


def trigger_by_pkey(
    analysis_function_id: str,
    target_model_pkey: int,
    target_model_name: str = "die",
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger analysis.

    Args:
        analysis_function_id: Name of the function to trigger.
        target_model_pkey: pkey of the target model to upload to.
        target_model_name: 'device', 'die' or 'wafer'.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/analysis/"
    parameters = parameters or {}
    params = {
        "analysis_function_id": analysis_function_id,
        "target_model_pkey": target_model_pkey,
        "target_model": target_model_name,
    }
    json_parameters = json.dumps(parameters)

    r = post(url, params=params, json=json_parameters)
    if r.status_code != 200:
        raise requests.HTTPError(r.text)
    return r


def trigger_device_data(
    project_id: str,
    device_id: str,
    analysis_function_id: str,
    parameters: dict | None = None,
) -> list[Analysis]:
    """Trigger device data analysis.

    Args:
        project_id: Name of the project to upload to.
        device_id: Name of the device to upload to.
        analysis_function_id: Name of the function to trigger.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/device_data/{project_id}/{device_id}/model_data"
    response = get(url)

    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    device_data_count = len(response.json())
    device_data_pkeys = [device_data["pkey"] for device_data in response.json()]

    if device_data_count == 0:
        raise ValueError(f"No device data found for {project_id}/{device_id}")

    analyses = []

    for device_data_pkey in device_data_pkeys:
        r = trigger_by_pkey(
            analysis_function_id=analysis_function_id,
            target_model_pkey=device_data_pkey,
            target_model_name="device_data",
            parameters=parameters,
        )
        if r.status_code != 200:
            raise requests.HTTPError(r.text)

        analyses.append(Analysis(**r.json()))
    return analyses


def trigger_device_data_multi(
    device_data_pkeys: list[int],
    analysis_function_id: str,
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> list[Analysis]:
    """Trigger multiple device analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        device_data_pkeys: List of unique device ids to trigger.
        analysis_function_id: Name of the function to trigger.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for did, params in zip(device_data_pkeys, parameters):
            futures.append(
                e.submit(
                    trigger_by_pkey,
                    target_model_pkey=did,
                    target_model_name="device_data",
                    analysis_function_id=analysis_function_id,
                    parameters=params,
                )
            )
        analysis_list: list[Analysis] = []
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))

        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))
        return analysis_list


def trigger_device_data_multi_by_pkeys(
    device_data_pkeys: list[int],
    analysis_function_id: str,
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> list[Analysis]:
    """Trigger multiple device analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        device_data_pkeys: List of unique device pkeys to trigger.
        analysis_function_id: Name of the function to trigger.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for did, params in zip(device_data_pkeys, parameters):
            futures.append(
                e.submit(
                    trigger_by_pkey,
                    target_model_pkey=did,
                    target_model_name="device_data",
                    analysis_function_id=analysis_function_id,
                    parameters=params,
                )
            )
        analysis_list: list[Analysis] = []
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))

        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))
        return analysis_list


def trigger_die(
    project_id: str,
    analysis_function_id: str,
    wafer_id: str,
    die_x: int,
    die_y: int,
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger die analysis.

    Args:
        project_id: Name of the project to upload to.
        analysis_function_id: Name of the function to trigger.
        wafer_id: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/die/{project_id}/{wafer_id}/{die_x}/{die_y}/"
    response = get(url)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    target_model_pkey = response.json()["pkey"]
    parameters = parameters or {}

    params = {
        "project_id": project_id,
        "analysis_function_id": analysis_function_id,
        "target_model": "die",
        "target_model_pkey": target_model_pkey,
    }

    url = f"{base_url}/analysis/"
    json_parameters = json.dumps(parameters)
    return post(url, params=params, json=json_parameters)


def trigger_die_multi(
    project_id: str,
    analysis_function_id: str,
    wafer_ids: list[str],
    die_xs: list[int],
    die_ys: list[int],
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> None:
    """Trigger multiple die analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        project_id: project name to trigger analysis to.
        analysis_function_id: Name of the function to trigger.
        wafer_ids: List of wafer names to upload to.
        die_xs: List of X coordinates of the dies to upload to.
        die_ys: List of Y coordinates of the dies to upload to.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    dies = set(zip(die_xs, die_ys))

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for wafer in wafer_ids:
            for die_x, die_y in dies:
                for params in parameters:
                    futures.append(
                        e.submit(
                            trigger_die,
                            project_id=project_id,
                            wafer_id=wafer,
                            die_x=die_x,
                            die_y=die_y,
                            analysis_function_id=analysis_function_id,
                            parameters=params,
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


def trigger_wafer(
    project_id: str,
    analysis_function_id: str,
    wafer_id: str,
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger wafer analysis.

    Args:
        project_id: Name of the project to upload to.
        analysis_function_id: Name of the function to trigger.
        wafer_id: name of the wafer to upload to.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/wafer/{project_id}/{wafer_id}"
    response = get(url)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    target_model_pkey = response.json()["pkey"]
    parameters = parameters or {}

    params = {
        "project_id": project_id,
        "analysis_function_id": analysis_function_id,
        "target_model": "wafer",
        "target_model_pkey": target_model_pkey,
    }

    url = f"{base_url}/analysis/"
    json_parameters = json.dumps(parameters)
    return post(url, params=params, json=json_parameters)


def get_wafer_analysis_plots(
    project_id: str,
    wafer_id: str,
    target_model: Literal["device_data", "die", "wafer"],
) -> Sequence[Image.Image]:
    """Get plots for a wafer.

    Args:
        project_id: Name of the project to upload to.
        wafer_id: Name of the wafer to upload to.
        target_model: Whether to get device_data analyses or die analyses.
    """
    analyses = get_analyses_for_wafer(
        project_id=project_id, wafer_id=wafer_id, target_model=target_model
    )

    if not analyses:
        raise LookupError(
            f"Could not find analyses for {target_model=!r}, {project_id=!r} and {wafer_id=!r}."
        )

    return _get_analysis_plots(analyses)


def get_die_analysis_plots(
    project_id: str, wafer_id: str, die_x: int, die_y: int
) -> list[Image.Image]:
    """Get plots for a die.

    Args:
        project_id: Name of the project to upload to.
        wafer_id: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.
    """
    analyses = get_analyses_for_die(
        project_id, wafer_id, die_x, die_y, target_model="die"
    )

    if not analyses:
        raise LookupError(
            f"Could not find analyses for {die_x=} die_y {die_y=} and {project_id=!r}."
        )

    return _get_analysis_plots(analyses)


def get_device_data_analysis_plots(
    project_id: str,
    device_id: str,
    wafer_id: str | None = None,
    die_x: int | None = None,
    die_y: int | None = None,
) -> Sequence[Image.Image]:
    """Get plots for a device data.

    Args:
        project_id: Name of the project to upload to.
        device_id: Name of the device to upload to.
        wafer_id: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.

    """
    analyses = get_analyses_for_device_data(
        project_id=project_id,
        device_id=device_id,
        wafer_id=wafer_id,
        die_x=die_x,
        die_y=die_y,
    )
    if not analyses:
        raise LookupError("Could not find analyses for device data.")

    return _get_analysis_plots(analyses)


def _fetch_plot(analysis: Analysis) -> Image.Image:
    """Fetch plot for a given analysis."""
    url = f"{base_url}/analysis/{analysis.pkey}/summary_plot"
    response = get(url)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)
    return Image.open(BytesIO(response.content)).convert("RGB")


def _get_analysis_plots(
    analyses: Sequence[Analysis],
    n_threads: int = settings.n_threads,
) -> list[Image.Image]:
    """Get plots for a list of analyses.

    Args:
        analyses: List of analyses to get plots for.
        n_threads: Number of threads to use for the upload.
    """
    plots: list[Image.Image] = []

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        future_plots = list(executor.map(_fetch_plot, analyses))

    plots.extend(future_plots)
    return plots
