import pytest
from sqlalchemy.sql import ColumnElement
from sqlmodel.sql.expression import SelectOfScalar
from sqlmodel import select
from doplaydo.dodata_core.models import Cell, Project, DeviceData, Device, Die, Wafer
import doplaydo.dodata as dd


@pytest.mark.skip(reason="fixme")
@pytest.mark.parametrize(
    ["clauses", "count"],
    [
        pytest.param(
            [
                dd.Project.project_id == "spirals_test",
                dd.Device.device_id
                == "RibLoss_cutback_rib_assembled_MFalse_W0p3_L0_20150_60150",
                dd.Die.x == 0,
                dd.Die.y == 0,
            ],
            1,
            id="die_x_0",
        ),
    ],
    ids=lambda data: data[0],
)
def test_data(clauses: list[ColumnElement[bool]], count: int) -> None:
    data = dd.db.device_data.get_data_by_query(clauses=clauses)

    assert len(data) == count
