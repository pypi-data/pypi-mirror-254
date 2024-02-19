"""This module contains the power_envelope function."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt
import doplaydo.dodata as dd


def run(
    device_data_pkey: int,
    n: int = 500,
    wvl_of_interest_nm: float = 1550,
    xkey: str = "wavelength",
    ykey: str = "output_power",
) -> dict[str, Any]:
    """Returns the smoothen data using a window averaging of a 1d array.

    Args:
        device_data_pkey: device data pkey.
        n: points per window.
        wvl_of_interest_nm: wavelength of interest.
        xkey: xkey.
        ykey: ykey.
    """
    data = dd.get_data_by_pkey(device_data_pkey)

    if data is None:
        raise ValueError(f"Device data with pkey {device_data_pkey} not found.")

    if xkey not in data:
        raise ValueError(
            f"Device data with pkey {device_data_pkey} does not have xkey {xkey!r}."
        )

    if ykey not in data:
        raise ValueError(
            f"Device data with pkey {device_data_pkey} does not have ykey {ykey!r}."
        )

    wavelength = data[xkey].values
    power = data[ykey].values

    closest_wvl_index = np.argmin(np.abs(wavelength - wvl_of_interest_nm))

    mean_curve = (
        data.output_power.rolling(n, center=True).mean().rolling(n, center=True).mean()
    )
    low_curve = (
        data.output_power.rolling(n, center=True).min().rolling(n, center=True).mean()
    )
    high_curve = (
        data.output_power.rolling(n, center=True).max().rolling(n, center=True).mean()
    )

    fig = plt.figure()
    plt.plot(wavelength, power, label="signal", zorder=0)
    plt.plot(wavelength, mean_curve, label="mean", zorder=1)
    plt.plot(wavelength, high_curve, label="high", zorder=1)
    plt.plot(wavelength, low_curve, label="low", zorder=1)
    plt.legend()
    plt.title(f"Envelope with Window Size {n}")
    plt.close()

    return dict(
        output={
            "closest_wavelength_value_nm": float(wavelength[closest_wvl_index]),
            "mean_wavelength_value_nm": float(mean_curve[closest_wvl_index]),
            "low_wavelength_value_nm": float(low_curve[closest_wvl_index]),
            "high_wavelength_value_nm": float(high_curve[closest_wvl_index]),
        },
        summary_plot=fig,
        device_data_pkey=device_data_pkey,
    )


if __name__ == "__main__":
    d = run(77404)
    print(d["output"]["closest_wavelength_value_nm"])
