# ruff: noqa: D415, UP007, D103
"""DoData functions for projects."""
from __future__ import annotations

import requests

from .common import url as base_url, post


def create(
    project_id: str,
    cell_id: str,
    parent_cell_id: str | None = None,
    x: float | None = None,
    y: float | None = None,
    angle: float | None = None,
    mirror: bool | None = None,
    attributes: dict[str, int | float | str] | None = None,
) -> requests.Response:
    """Create a new device for an existing cell in DoData.

    Args:
        project_id: Name of the project to create the cell in.
        cell_id: Name of the cell.
        parent_cell_id: Optional parent cell (reference frame) of the device.
        x: x-coordinate of the device.
        y: y-coordinate of the device.
        angle: Angle of the device (range: [0,360)).
        mirror: Whether the device is mirrored in the reference frame.
        attributes: Additional information about the device.
            Must be a one-dimensional dictionary with int/float/str values.


    Example:
        dd.api.device.create(
            project_id="TEST",
            cell_id="test_cell",
        )
        dd.api.device.create(
            project_id="TEST",
            cell_id="test_cell",
            x=500,
            y=0,
            angle=180,
            mirror=False,
        )
    """
    optional_parameters = [parent_cell_id, x, y, angle, mirror]
    if any([p is not None for p in optional_parameters]) and not all(
        [p is not None for p in optional_parameters]
    ):
        raise ValueError(
            "If any of parent_cell_id, x, y, angle, mirror are defined,"
            " all must be defined."
        )
    url = f"{base_url}/device"
    params = {
        "project_id": project_id,
        "cell_id": cell_id,
        "parent_cell_id": parent_cell_id,
        "x": x,
        "y": y,
        "angle": angle,
        "mirror": mirror,
    }
    return post(url, params=params, data={"attributes": attributes or {}})
