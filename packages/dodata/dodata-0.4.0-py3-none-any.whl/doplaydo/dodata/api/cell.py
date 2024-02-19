# ruff: noqa: D415, UP007, D103
"""DoData functions for projects."""
from __future__ import annotations

import requests

from .common import url as base_url, post


def create(
    project_id: str,
    cell_id: str,
    attributes: dict[str, int | float | str] | None = None,
) -> requests.Response:
    """Create a new cell for an existing project in DoData.

    Args:
        project_id: Name of the project to create the cell in.
        cell_id: Name of the cell.
        attributes: Additional information about the cell.
            Must be a one-dimensional dictionary with int/float/str values.

    Example:
        dd.api.cell.create(
            project_id="TEST",
            cell_id="test_cell"
        )
    """
    url = f"{base_url}/cell"
    params = {"project_id": project_id, "cell_id": cell_id}
    return post(url, params=params, data={"attributes": attributes or {}})
