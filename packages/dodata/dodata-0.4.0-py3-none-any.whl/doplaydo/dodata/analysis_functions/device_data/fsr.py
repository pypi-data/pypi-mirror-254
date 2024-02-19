"""Free spectral range (FSR) analysis."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import doplaydo.dodata as dd


def find_resonance_peaks(
    y, height: float = 0.1, threshold: None | float = None, distance: float | None = 10
):
    """Find the resonance peaks in the ring resonator response.

    'height' and 'distance' can be adjusted based on the specifics of your data.

    Args:
        y: ndarray
        height : number or ndarray or sequence, optional
            Required height of peaks. Either a number, ``None``, an array matching
            `x` or a 2-element sequence of the former. The first element is
            always interpreted as the  minimal and the second, if supplied, as the
            maximal required height.
        threshold : number or ndarray or sequence, optional
            Required threshold of peaks, the vertical distance to its neighboring
            samples. Either a number, ``None``, an array matching `x` or a
            2-element sequence of the former. The first element is always
            interpreted as the  minimal and the second, if supplied, as the maximal
            required threshold.
        distance : number, optional
            Required minimal horizontal distance (>= 1) in samples between
            neighbouring peaks. Smaller peaks are removed first until the condition
            is fulfilled for all remaining peaks.
    """
    if height < 0:
        y = -y
        height = abs(height)

    peaks, _ = find_peaks(y, height=height, distance=distance)
    return peaks


def remove_baseline(wavelength: np.ndarray, power: np.ndarray, deg: int = 4):
    """Return power corrected without baseline.

    Fit a polynomial ``p(x) = p[0] * x**deg + ... + p[deg]`` of degree `deg`
    """
    pfit = np.polyfit(wavelength - np.mean(wavelength), power, deg)
    power_baseline = np.polyval(pfit, wavelength - np.mean(wavelength))

    power_corrected = power - power_baseline
    power_corrected = power_corrected + max(power_baseline) - max(power)
    return power_corrected


def run(
    device_data_pkey: int,
    height: float = -0.1,
    threshold: None | float = None,
    distance: float | None = 10,
    xkey: str = "wavelength",
    ykey: str = "output_power",
) -> dict[str, Any]:
    """Returns the Free spectral range (FSR) for a resonator.

    Args:
        device_data_pkey: The pkey of the device data to be analyzed.
        height: Required height of peaks. <0 for minima.
        threshold: Required threshold of peaks, the vertical distance to its neighboring.
        distance: Required minimal horizontal distance (>= 1) in samples between.
        xkey: The key of the x data in the device data.
        ykey: The key of the y data in the device data.
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

    x = data[xkey].values
    y = data[ykey].values
    spectrum = y
    spectrum_normalized = remove_baseline(wavelength=x, power=y, deg=4)

    peaks = find_resonance_peaks(
        spectrum_normalized, height=height, distance=distance, threshold=threshold
    )

    if not peaks.any():
        raise ValueError(
            f"No peaks found for device data with pkey {device_data_pkey}, adjust height {height}."
        )

    peak_frequencies = x[peaks]
    fsr = np.diff(peak_frequencies)
    fsr_mean = np.mean(fsr)
    fsr_std = np.std(fsr)

    fig = plt.figure()
    plt.plot(x, spectrum, label="spectrum")
    plt.plot(x[peaks], spectrum[peaks], "x", color="red", label="Peaks")
    plt.legend()
    plt.title(f"FSR: {fsr_mean:.2f} ± {fsr_std:.2f} nm")

    if len(peaks) < 2:
        raise ValueError(
            f"Only one peak found for device data with pkey {device_data_pkey}, adjust height {height}."
        )

    if len(peaks) > 200:
        raise ValueError(
            f"More than 200 peaks found for device data with pkey {device_data_pkey}, adjust height {height}."
        )

    return dict(
        output={
            "fsr_mean": float(fsr_mean),
            "fsr_std": float(fsr_std),
            "peaks": x[peaks].tolist() or None,
            "fsr": fsr.tolist() or None,
        },
        summary_plot=fig,
        device_data_pkey=device_data_pkey,
    )


if __name__ == "__main__":
    d = run(82766, height=-0.01)
    print(d["output"]["fsr_mean"])
