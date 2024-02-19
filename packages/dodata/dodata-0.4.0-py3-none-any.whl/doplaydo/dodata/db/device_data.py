"""Functions for querying device data from the database."""
import pandas as pd
from .. import session, settings, ParentCell
from ..api.device_data import get_data_by_pkey
from doplaydo.dodata_core.models import Cell, Project, DeviceData, Device, Die, Wafer
from sqlalchemy.sql import ColumnElement
from sqlmodel import select
from sqlmodel.sql.expression import SelectOfScalar
from tqdm.auto import tqdm

import requests
from concurrent.futures import ProcessPoolExecutor


def _get_device_data_joined_query() -> SelectOfScalar[DeviceData]:
    return (
        select(DeviceData)
        .join(Device)
        .join(Die, isouter=True)
        .join(Cell, Device.cell_pkey == Cell.pkey)  # type: ignore[arg-type]
        .join(ParentCell, Device.parent_cell_pkey == ParentCell.pkey, isouter=True)  # type: ignore[arg-type]
        .join(Project, Project.pkey == Cell.project_pkey)  # type: ignore[arg-type]
        .join(Wafer, Wafer.pkey == Die.wafer_pkey, isouter=True)  # type: ignore[arg-type]
    )


def _get_device_data_and_frame(idx: int) -> tuple[int, pd.DataFrame]:
    return (idx, get_data_by_pkey(idx))


def get_data_by_query(
    clauses: list[ColumnElement[bool]] = [],
    multi_processing: bool = True,
    progress_bar: bool = False,
    limit: int | None = None,
) -> list[tuple[DeviceData, pd.DataFrame]]:
    """Query the database for device data and return DeviceData and its raw data.

    Args:
        clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        multi_processing: Use multiple processes to download data from the API
            endpoint.
        progress_bar: Show a progress bar.
        limit: Limit the number of results returned.
    """
    statement = _get_device_data_joined_query()

    for clause in clauses:
        statement = statement.where(clause)

    if limit:
        statement = statement.limit(limit)

    _dd = session.exec(statement).all()

    device_data = {dd.pkey: dd for dd in _dd}

    if multi_processing:
        with ProcessPoolExecutor(max_workers=settings.n_cores) as executor:
            try:
                mp_data = executor.map(_get_device_data_and_frame, device_data.keys())
                results: list[tuple[DeviceData, pd.DataFrame]] = []
                if progress_bar:
                    for result in tqdm(mp_data, total=len(device_data)):
                        results.append((device_data[result[0]], result[1]))
                else:
                    for result in mp_data:
                        results.append((device_data[result[0]], result[1]))
                return results
            except requests.HTTPError:
                executor.shutdown(wait=False, cancel_futures=True)
                raise
    else:
        if progress_bar:
            data = [
                _get_device_data_and_frame(idx)  # type:ignore[arg-type]
                for idx in tqdm(device_data.keys(), total=len(device_data))
            ]
            return [(device_data[_pkey], _data) for _pkey, _data in data]
        else:
            data = [_get_device_data_and_frame(idx) for idx in device_data.keys()]  # type:ignore[arg-type]
            return [(device_data[_pkey], _data) for _pkey, _data in data]


def get_data_objects_by_query(
    clauses: list[ColumnElement[bool]] = [],
    multi_processing: bool = True,
    progress_bar: bool = False,
    limit: int | None = None,
) -> list[DeviceData]:
    """Query the database for device data and return DeviceData and its raw data.

    Args:
        clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        multi_processing: Use multiple processes to download data from the API
            endpoint.
        progress_bar: Show a progress bar.
        limit: Limit the number of results returned.
    """
    statement = _get_device_data_joined_query()

    for clause in clauses:
        statement = statement.where(clause)

    if limit:
        statement = statement.limit(limit)

    return list(session.exec(statement).all())
