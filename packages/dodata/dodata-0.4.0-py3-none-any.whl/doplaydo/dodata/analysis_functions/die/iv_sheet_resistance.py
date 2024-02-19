"""Fits sheet resistance from an IV curve and returns Sheet resistance Ohms/sq."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt
import doplaydo.dodata as dd


def run(
    die_pkey: int,
    width_key: str = "width_um",
    length_key: str = "length_um",
    length_value: float = 20,
) -> dict[str, Any]:
    """Fits sheet resistance from an IV curve and returns Sheet resistance Ohms/sq.

    It assumes fixed length and sweeps width.

    Args:
        die_pkey: pkey of the device data to analyze.
        width_key: key of the width attribute to filter by.
        width_value: value of the width attribute to filter by.
        length_key: key of the length attribute to filter by.
        length_value: value of the length attribute to filter by.
    """
    device_data_objects = dd.get_data_by_query(
        [
            dd.Die.pkey == die_pkey,
            dd.attribute_filter(dd.Cell, length_key, length_value),
        ]
    )

    if not device_data_objects:
        raise ValueError(
            f"No device die found with die_pkey {die_pkey}, length_key {length_key!r}, length_value {length_value}"
        )

    resistances = []
    widths_um = []
    lengths_um = []
    areas = []

    for device_data, df in device_data_objects:
        length_um = device_data.device.cell.attributes.get(length_key)
        width_um = device_data.device.cell.attributes.get(width_key)
        lengths_um.append(length_um)
        widths_um.append(width_um)
        i = df.i  # type: ignore[arg-type, call-arg]
        v = df.v  # type: ignore[arg-type, call-arg]
        p = np.polyfit(i, v, deg=1)
        resistances.append(p[0])
        area = length_um * width_um
        areas.append(area)

    p = np.polyfit(areas, resistances, deg=1)
    sheet_resistance = p[0]
    areas_fit = np.linspace(np.min(areas), np.max(areas), 3)
    resistances_fit = np.polyval(p, areas_fit)

    fig = plt.figure()
    plt.plot(areas, resistances, label="iv", zorder=0)
    plt.plot(areas_fit, resistances_fit, label="fit", zorder=1)
    plt.xlabel("Areas (um^2)")
    plt.ylabel("V (V)")
    plt.legend()
    plt.title(f"Sheet Resistance {sheet_resistance:.2f} Ohms/sq")

    return dict(
        output={
            "sheet_resistance": float(sheet_resistance),
        },
        summary_plot=fig,
        die_pkey=die_pkey,
    )


if __name__ == "__main__":
    d = run(11)
    print(d["output"]["sheet_resistance"])
