"""Calculates loss per component."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt

import doplaydo.dodata as dd


def run(die_pkey: int, key: str = "components") -> dict[str, Any]:
    """Returns component loss in dB/component.

    Args:
        die_pkey: pkey of the die to analyze.
        key: attribute key to filter by.
    """
    device_data_objects = dd.get_data_by_query(
        [
            dd.Die.pkey == die_pkey,
        ]
    )

    if not device_data_objects:
        raise ValueError(f"No device data found with die_pkey {die_pkey}, key {key!r}")

    powers = []
    components = []

    for device_data, df in device_data_objects:
        if not device_data.device.cell.attributes.get(key):
            raise ValueError(
                f"No attribute {key!r} found for die_pkey {die_pkey}, device_pkey {device_data.device.pkey}"
            )
        components.append(device_data.device.cell.attributes.get(key))
        powers.append(df.output_power.max())

    p = np.polyfit(components, powers, 1)
    component_loss = -p[0]

    fig = plt.figure()
    plt.plot(components, powers, "o")
    plt.plot(components, np.polyval(p, components), "r-", label="fit")

    plt.xlabel("Number of components")
    plt.ylabel("Power (dBm)")
    plt.title(f"loss = {-p[0]:.2f} dB/component")

    return dict(
        output={"component_loss": component_loss},
        summary_plot=fig,
        die_pkey=die_pkey,
    )


if __name__ == "__main__":
    d = run(11845)
    print(d["output"]["component_loss"])
