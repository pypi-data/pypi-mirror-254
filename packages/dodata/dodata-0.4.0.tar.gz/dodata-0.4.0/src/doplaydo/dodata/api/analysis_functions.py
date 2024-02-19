"""Common API calls to analysis_functions."""
from __future__ import annotations


import json
import requests
from .common import url as base_url, post


def validate(
    analysis_function_id: str,
    function_path: str,
    test_model_pkey: int,
    target_model_name: str = "device_data",
    parameters: dict | None = None,
) -> requests.Response:
    """Validates an analysis function.

    Args:
        analysis_function_id: Name of the function to trigger.
        function_path: Path to the file to be uploaded.
        test_model_pkey: pkey of the target model to upload to.
        target_model_name: 'device', 'die' or 'wafer'.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/analysis_functions/validate_function"
    params = {
        "analysis_function_id": analysis_function_id,
        "test_model_pkey": test_model_pkey,
        "target_model_name": target_model_name,
    }
    data = {
        "test_kwargs": json.dumps(parameters) if parameters else "{}",
    }

    function_path = str(function_path)
    with open(function_path, "rb") as f:
        files = {"script": (function_path, f.read())}
        response = post(url, params=params, files=files, data=data)

    if response.status_code != 200:
        print(response.text)

    else:
        print(response.headers)

    return response


def _upload(
    analysis_function_id: str,
    function_path: str,
    test_model_pkey: int,
    target_model_name: str = "device_data",
) -> requests.Response:
    """Uploads an analysis function.

    Args:
        analysis_function_id: Name of the function to trigger.
        function_path: Path to the file to be uploaded.
        test_model_pkey: pkey of the target model to upload to.
        target_model_name: 'device', 'die' or 'wafer'.
    """
    url = f"{base_url}/analysis_functions"
    params = {
        "analysis_function_id": analysis_function_id,
        "test_model_pkey": test_model_pkey,
        "target_model_name": target_model_name,
    }

    function_path = str(function_path)
    with open(function_path, "rb") as f:
        files = {"script": (function_path, f)}
        response = post(url, params=params, files=files)

    return response


def validate_and_upload(
    analysis_function_id: str,
    function_path: str,
    test_model_pkey: int,
    target_model_name: str = "device_data",
    parameters: dict | None = None,
) -> requests.Response:
    """Validates and uploads an analysis function.

    Args:
        analysis_function_id: Name of the function to trigger.
        function_path: Path to the file to be uploaded.
        test_model_pkey: pkey of the target model to upload to.
        target_model_name: 'device', 'die' or 'wafer'.
        parameters: for triggering analysis.
    """
    response_validate = validate(
        analysis_function_id,
        function_path,
        test_model_pkey,
        target_model_name,
        parameters,
    )
    if response_validate.status_code == 200:
        _upload(analysis_function_id, function_path, test_model_pkey, target_model_name)

    return response_validate
