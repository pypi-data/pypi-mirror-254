"""This module contains functions for querying the database for analysis objects."""
from .. import session, select
from doplaydo.dodata_core.models import (
    Die,
    Wafer,
    Project,
    Analysis,
    AnalysisFunction,
    DeviceData,
    Device,
    Cell,
)
from collections.abc import Sequence
from sqlmodel import SQLModel
from sqlalchemy.sql import ColumnElement
from sqlmodel.sql.expression import SelectOfScalar

from typing import Literal


def _get_analyses_joined_query(
    target_model: Literal["device_data", "die", "wafer"],
) -> SelectOfScalar[Analysis]:
    match target_model:
        case "device_data":
            query = (
                select(Analysis)
                .join(DeviceData, onclause=Analysis.device_data_pkey == DeviceData.pkey)
                .join(Device)
                .join(Cell, onclause=Device.cell_pkey == Cell.pkey)
                .join(Die, onclause=DeviceData.die_pkey == Die.pkey, isouter=True)
                .join(Wafer, onclause=Die.wafer_pkey == Wafer.pkey, isouter=True)
                .join(AnalysisFunction)
            )
        case "die":
            query = (
                select(Analysis)
                .join(Die, onclause=Analysis.die_pkey == Die.pkey)
                .join(Wafer, onclause=Die.wafer_pkey == Wafer.pkey)
                .join(DeviceData, onclause=Die.pkey == DeviceData.die_pkey)
                .join(Device)
                .join(Cell, onclause=Device.cell_pkey == Cell.pkey)
                .join(AnalysisFunction)
            )
        case "wafer":
            query = (
                select(Analysis)
                .join(Wafer, onclause=Analysis.wafer_pkey == Wafer.pkey)
                .join(Die, onclause=Die.wafer_pkey == Wafer.pkey, isouter=False)
                .join(DeviceData, onclause=Die.pkey == DeviceData.die_pkey)
                .join(Device, onclause=DeviceData.device_pkey == Device.pkey)
                .join(Cell, onclause=Device.cell_pkey == Cell.pkey)
                .join(AnalysisFunction)
            )
        case _:
            raise ValueError(
                f"{target_model=} must be one of the following: 'device_data', 'die', or 'wafer'."
            )

    return query.distinct()


def get_analyses_by_query(
    target_model: Literal["device_data", "die", "wafer"],
    clauses: list[ColumnElement[bool]],
) -> Sequence[Analysis]:
    """Query the database for device data and return DeviceData and its raw data.

    Args:
        target_model: Whether to get analyses through wafer, die, or device_data.
        clauses: sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
    """
    statement = _get_analyses_joined_query(target_model)

    for clause in clauses:
        statement = statement.where(clause)

    _analyses = session.exec(statement).all()

    return _analyses


def get_analyses_for_device_data(
    project_id: str,
    device_id: str,
    wafer_id: str | None = None,
    die_x: int | None = None,
    die_y: int | None = None,
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
) -> Sequence[Analysis]:
    """Get all analyses for device_data.

    Args:
        project_id: The name of the project.
        device_id: The name of the device.
        wafer_id: The name of the wafer.
        die_x: The x coordinate of the die.
        die_y: The y coordinate of the die.
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
    """
    query = (
        select(DeviceData)
        .join(Device)
        .join(Cell, Device.cell_pkey == Cell.pkey)
        .join(Project)
        .where(Project.project_id == project_id)
        .where(Device.device_id == device_id)
    )

    if die_x is not None or die_y is not None:
        query = query.join(Die, DeviceData.die_pkey == Die.pkey)

        if die_x is not None:
            query = query.where(Die.x == die_x)

        if die_y is not None:
            query = query.where(Die.y == die_y)

    if wafer_id:
        query = query.join(Wafer).where(Wafer.wafer_id == wafer_id)

    device_data = session.exec(query).all()
    if not device_data:
        raise LookupError("Could not find device_data in the database.")

    statement = select(Analysis).where(
        Analysis.device_data_pkey.in_([d.pkey for d in device_data])
    )
    for clause in filter_clauses:
        statement = statement.where(clause)

    if limit:
        statement = statement.limit(limit)

    return session.exec(statement).all()


def get_analyses_for_die(
    project_id: str,
    wafer_id: str,
    die_x: int,
    die_y: int,
    target_model: Literal["device_data", "die"],
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
) -> Sequence[Analysis]:
    """Get all analyses for a die.

    Args:
        project_id: The name of the project.
        wafer_id: The name of the wafer.
        die_x: The x coordinate of the die.
        die_y: The y coordinate of the die.
        target_model: Which analyses to aggregate, either device_data analyses
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
    """
    die = session.exec(
        select(Die)
        .join(Wafer)
        .join(Project)
        .where(Wafer.wafer_id == wafer_id)
        .where(Project.project_id == project_id)
        .where(Die.x == die_x)
        .where(Die.y == die_y)
    ).one_or_none()
    if die is None:
        raise LookupError(
            f"Could not find die {(die_x,die_y)} for wafer {wafer_id} "
            f"in project {project_id} in the database."
        )

    return get_analyses_for_die_by_pkey(
        die_pkey=die.pkey,
        filter_clauses=filter_clauses,
        limit=limit,
        test_die_pkey=False,
        target_model=target_model,
    )


def get_analyses_for_die_by_pkey(
    die_pkey: int,
    target_model: Literal["device_data", "die"],
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
    test_die_pkey: bool = True,
) -> Sequence[Analysis]:
    """Get all analyses for a die.

    Args:
        die_pkey: The pkey of the die.
        target_model: Which analyses to aggregate, either device_data analyses
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
        test_die_pkey: Check whether the die exists first.
    """
    if test_die_pkey:
        die = session.get(Die, die_pkey)
        if die is None:
            raise LookupError(f"Could not find die {die_pkey} in the database.")

    statement = _get_analyses_joined_query(target_model).where(Die.pkey == die_pkey)
    for clause in filter_clauses:
        statement = statement.where(clause)
    if limit:
        statement = statement.limit(limit)

    return session.exec(statement).all()


def get_analyses_for_wafer(
    project_id: str,
    wafer_id: str,
    target_model: Literal["device_data", "die", "wafer"],
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
) -> Sequence[Analysis]:
    """Get all analyses for a wafer.

    Args:
        project_id: The name of the project.
        wafer_id: The name of the wafer.
        target_model: Which analyses to aggregate, either device_data analyses
            or die analyses.
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
    """
    wafer = session.exec(
        select(Wafer)
        .join(Project)
        .where(Wafer.wafer_id == wafer_id)
        .where(Project.project_id == project_id)
    ).one_or_none()
    if not wafer:
        raise LookupError("Could not find wafer in the database.")
    return get_analyses_for_wafer_by_pkey(
        wafer_pkey=wafer.pkey,
        filter_clauses=filter_clauses,
        limit=limit,
        target_model=target_model,
    )


def get_analyses_for_wafer_by_pkey(
    wafer_pkey: int,
    target_model: Literal["device_data", "die", "wafer"],
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
) -> Sequence[Analysis]:
    """Get all analyses for a wafer.

    Args:
        wafer_pkey: The pkey of the wafer.
        target_model: Which analyses to aggregate, either device_data analyses
            or die analyses.
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
    """
    statement = _get_analyses_joined_query(target_model=target_model).where(
        Wafer.pkey == wafer_pkey
    )
    for clause in filter_clauses:
        statement = statement.where(clause)
    if limit:
        statement = statement.limit(limit)

    return session.exec(statement).all()


def _get_target_model(
    target_model_name: Literal["wafer", "die", "device_data"],
) -> type[SQLModel]:
    """Get the sqlmodel by name."""
    match target_model_name:
        case "wafer":
            return Wafer
        case "die":
            return Die
        case "device_data":
            return DeviceData
        case _:
            raise ValueError(f"Unknown {target_model_name=}")


def get_analyses_by_pkey(
    target_model_pkey: int,
    target_model: Literal["device_data", "die", "wafer"],
    filter_clauses: list[ColumnElement[bool]] = [],
    limit: int | None = None,
    test_pkey: bool = True,
) -> Sequence[Analysis]:
    """Get all analyses for a wafer.

    Args:
        target_model_pkey: The pkey of the wafer/die/device_data pkey.
        target_model: Which analyses to aggregate, either device_data analyses
            or die analyses or wafer analyses.
        filter_clauses: A list of sql expressions such as `dd.Cell.cell_id == "RibLoss"`.
        limit: Limit the number of results returned.
        test_pkey: Check whether the wafer/die/device_data exists first.
    """
    model = _get_target_model(target_model)
    if test_pkey:
        target = session.get(model, target_model_pkey)
        if target is None:
            raise LookupError(
                f"Could not find {target_model=} {target_model_pkey=} in the database."
            )
    statement = _get_analyses_joined_query(target_model=target_model).where(
        model.pkey == target_model_pkey
    )
    for clause in filter_clauses:
        statement = statement.where(clause)
    if limit:
        statement = statement.limit(limit)

    return session.exec(statement).all()
