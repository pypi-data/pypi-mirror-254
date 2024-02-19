"""Calculates propagation loss from cutback measurement."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt

import doplaydo.dodata as dd


def run(
    die_pkey: int,
    key: str = "width_um",
    value: float = 0.3,
    length_key: str = "length_um",
) -> dict[str, Any]:
    """Returns propagation loss in dB/cm.

    Args:
        die_pkey: pkey of the die to analyze.
        key: key of the attribute to filter by.
        value: value of the attribute to filter by.
        length_key: key of the length attribute.
    """
    device_data_objects = dd.get_data_by_query(
        [dd.Die.pkey == die_pkey, dd.attribute_filter(dd.Cell, key, value)]
    )

    if not device_data_objects:
        raise ValueError(
            f"No device data found with die_pkey {die_pkey}, key {key!r}, value {value}"
        )

    powers = []
    lengths_um = []

    for device_data, df in device_data_objects:
        lengths_um.append(device_data.device.cell.attributes.get(length_key))
        powers.append(df.output_power.max())

    p = np.polyfit(lengths_um, powers, 1)
    propagation_loss = p[0] * 1e4 * -1

    fig = plt.figure()
    plt.plot(lengths_um, powers, "o")
    plt.plot(lengths_um, np.polyval(p, lengths_um), "r-", label="fit")

    plt.xlabel("Length (um)")
    plt.ylabel("Power (dBm)")
    plt.title(f"Propagation loss {key}={value}: {p[0]*1e4*-1:.2f} dB/cm ")

    return dict(
        output={"propagation_loss_dB_cm": propagation_loss},
        summary_plot=fig,
        die_pkey=die_pkey,
    )


if __name__ == "__main__":
    d = run(7732)
    print(d["output"]["propagation_loss_dB_cm"])
