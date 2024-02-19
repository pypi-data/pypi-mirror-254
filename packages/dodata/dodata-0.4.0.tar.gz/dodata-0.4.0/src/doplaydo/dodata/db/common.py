"""Common utilities for the db portion of the sdk."""
from sqlmodel import cast, Boolean, Numeric, Integer, SQLModel
from sqlalchemy.sql import ColumnElement


def attribute_filter(
    model: SQLModel, key: str, filter_value: int | bool | float | str
) -> ColumnElement[bool]:
    """Filter data model attributes based on the specified key and value.

    Args:
        model (SQLModel): Database model representing the data.
        key (str): Key for the attribute to filter.
        filter_value (int | bool | float | str): Value to filter for.

    Raises:
        ValueError: If filter_value is not of type bool, str, float, or int.

    Returns:
        ColumnElement[bool]: A SQLAlchemy ColumnElement filtering condition.

    Example:
        import dodata_sdk as ddk
        ddk.attribute_filter(DeviceData, "measurement_type", "Spectrum")
        ddk.attribute_filter(Cell, "length_um", 15)
        ddk.attribute_filter(Wafer, "doping", 10e-18)
        ddk.attribute_filter(Analysis, "raised_flags", True)
    """
    if isinstance(filter_value, int):
        return cast(model.attributes[key], Integer) == filter_value
    elif isinstance(filter_value, float):
        return cast(model.attributes[key], Numeric) == filter_value
    elif isinstance(filter_value, bool):
        return cast(model.attributes[key], Boolean) == filter_value
    elif isinstance(filter_value, str):
        return model.attributes[key].astext == filter_value

    raise ValueError(
        "Can only filter attributes for strings, booleans, or numeric values."
    )
