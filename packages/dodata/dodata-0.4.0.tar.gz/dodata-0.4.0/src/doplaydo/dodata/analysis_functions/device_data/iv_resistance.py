"""Fits resistance from an IV curve."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt

import doplaydo.dodata as dd


def run(
    device_data_pkey: int,
    min_i: float | None = None,
    max_i: float | None = None,
    xkey: str = "i",
    ykey: str = "v",
) -> dict[str, Any]:
    """Fits resistance from an IV curve.

    Args:
        device_data_pkey: pkey of the device data to analyze.
        min_i: minimum intensity. If None, the minimum intensity is the minimum of the data.
        max_i: maximum intensity. If None, the maximum intensity is the maximum of the data.
        xkey: key of the x data.
        ykey: key of the y data.
    """
    data = dd.get_data_by_pkey(device_data_pkey)

    if xkey not in data:
        raise ValueError(
            f"Device data with pkey {device_data_pkey} does not have xkey {xkey!r}."
        )

    if ykey not in data:
        raise ValueError(
            f"Device data with pkey {device_data_pkey} does not have ykey {ykey!r}."
        )
    i = data[xkey].values
    v = data[ykey].values

    min_i = min_i or np.min(i)
    max_i = max_i or np.max(i)

    i2 = i[(i > min_i) & (i < max_i)]
    v2 = v[(i > min_i) & (i < max_i)]
    i, v = i2, v2

    p = np.polyfit(i, v, deg=1)

    i_fit = np.linspace(min_i, max_i, 3)
    v_fit = np.polyval(p, i_fit)
    resistance = p[0]

    fig = plt.figure()
    plt.plot(i, v, label="iv", zorder=0)
    plt.plot(i_fit, v_fit, label="fit", zorder=1)
    plt.xlabel("I (A)")
    plt.ylabel("V (V)")
    plt.legend()
    plt.title(f"Resistance {resistance:.2f} Ohms")
    plt.close()

    return dict(
        output={
            "resistance": float(resistance),
        },
        summary_plot=fig,
        device_data_pkey=device_data_pkey,
    )


if __name__ == "__main__":
    d = run(79366)
    print(d["output"]["resistance"])
