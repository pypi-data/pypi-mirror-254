"""This modules contains functions for querying the database for wafer objects."""
from doplaydo.dodata_core import models as m
from sqlmodel.sql.expression import SelectOfScalar
from sqlalchemy.sql import ColumnElement
from .. import session, select
from collections.abc import Sequence
from .die import _get_die_joined_query


def _get_wafer_joined_query() -> SelectOfScalar[m.Wafer]:
    return (
        select(m.Wafer)
        .join(m.Die)
        .join(m.Project, m.Wafer.project_pkey == m.Project.pkey)
        .join(m.Analysis, m.Analysis.wafer_pkey == m.Wafer.pkey, isouter=True)
        .join(
            m.AnalysisFunction,
            onclause=m.Analysis.analysis_function_pkey == m.AnalysisFunction.pkey,
            isouter=True,
        )
    )


def get_wafers_by_query(clauses: list[ColumnElement[bool] | bool]) -> Sequence[m.Wafer]:
    """Return a list of filtered wafers."""
    statement = _get_wafer_joined_query()

    for clause in clauses:
        statement = statement.where(clause)

    _wafers = session.exec(statement).all()

    return _wafers


def get_by_id(project_id: str, wafer_id: str) -> Sequence[m.Wafer]:
    """Get a wafer by project name and wafer name."""
    return get_wafers_by_query(
        [m.Project.project_id == project_id, m.Wafer.wafer_id == wafer_id]
    )


def get_by_pkey(wafer_pkey: int) -> m.Wafer:
    """Get a wafer by its unique pkey."""
    _wafers = get_wafers_by_query([m.Wafer.pkey == wafer_pkey])

    if not _wafers:
        raise ValueError(f"Could not find wafer with {wafer_pkey=}")

    return _wafers[0]


def get_wafer_dies(
    wafer_id: str, project_id: str, clauses: list[ColumnElement[bool] | bool]
) -> Sequence[m.Die]:
    """Return a list of filtered wafer dies."""
    statement = _get_die_joined_query()

    clauses.append(m.Project.project_id == project_id)
    clauses.append(m.Wafer.wafer_id == wafer_id)

    for clause in clauses:
        statement = statement.where(clause)

    _dies = session.exec(statement).all()

    return _dies
