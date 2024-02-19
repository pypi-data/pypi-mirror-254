import pathlib
import requests
import pytest
from sqlalchemy.sql import ColumnElement
from sqlmodel.sql.expression import SelectOfScalar
from sqlmodel import select
from doplaydo.dodata_core.models import Cell, Project, DeviceData, Device, Die, Wafer
import doplaydo.dodata as dd
from tqdm.auto import tqdm

module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent
notebooks_path = repo_path / "notebooks"
wafer_id = "6d4c615ff105"
spirals_data = notebooks_path / "spirals" / wafer_id

if __name__ == "__main__":
    spectrum_measurement_type = dd.api.device_data.PlottingKwargs(
        x_name="wavelength",
        y_name="output_power",
        x_col="wavelength",
        y_col=["output_power"],  # can also be a string for a single value
        # y_col="output_power",
    )

    MEASUREMENTS_PATH = spirals_data
    PROJECT_NAME = "spirals"
    data_files = list(MEASUREMENTS_PATH.glob("**/data.json"))
    project_ids = []
    device_ids = []
    die_xs = []
    die_ys = []
    wafer_ids = []
    plotting_kwargs = []
    data_types = []
    die_ids = []

    for path in data_files:
        device_id = path.parts[-2]
        die_id = path.parts[-3]
        die_x, die_y = die_id.split("_")
        wafer_id = path.parts[-4]

        device_ids.append(device_id)
        die_ids.append(die_id)
        die_xs.append(die_x)
        die_ys.append(die_y)
        wafer_ids.append(wafer_id)
        plotting_kwargs.append(spectrum_measurement_type)
        project_ids.append(PROJECT_NAME)
        data_types.append("measurement")

    die_set = set(die_ids)
    wafer_set = set(wafer_ids)
    database_dies = []

    widths_um = [0.3, 0.5, 0.8]
    parameters = [{"width_um": width_um} for width_um in widths_um]

    dd.analysis.trigger_die_multi(
        project_id=PROJECT_NAME,
        analysis_function_id="loss_cutback",
        wafer_ids=wafer_set,
        die_xs=die_xs,
        die_ys=die_ys,
        parameters=parameters,
        progress_bar=True,
        )
