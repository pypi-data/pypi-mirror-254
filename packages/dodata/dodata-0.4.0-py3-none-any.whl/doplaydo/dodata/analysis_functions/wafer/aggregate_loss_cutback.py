"""Aggregate analysis."""

from typing import Any
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

import doplaydo.dodata as dd


def plot_wafermap(
    losses: dict[tuple[int, int], float],
    lower_spec: float,
    upper_spec: float,
    metric: str,
    key: str,
    value: float | None = None,
) -> Figure:
    """Plot a wafermap of the losses.

    Args:
        losses: Dictionary of losses.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        metric: Metric to analyze.
        key: Key of the parameter to analyze.
        value: Value of the parameter to analyze.
    """
    fontsize = 20

    # Calculate the bounds and center of the data
    die_xs, die_ys = zip(*losses.keys())
    die_x_min, die_x_max = min(die_xs), max(die_xs)
    die_y_min, die_y_max = min(die_ys), max(die_ys)

    # Create the data array
    data = np.full((die_y_max - die_y_min + 1, die_x_max - die_x_min + 1), np.nan)
    for (i, j), v in losses.items():
        data[j - die_y_min, i - die_x_min] = v

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.8))

    # First subplot: Heatmap
    ax1.set_xlabel("Die X", fontsize=fontsize)
    ax1.set_ylabel("Die Y", fontsize=fontsize)
    title = f"{metric} {key}={value}" if value else f"{metric}"
    ax1.set_title(title, fontsize=fontsize, pad=10)

    cmap = plt.get_cmap("viridis")
    vmin, vmax = (
        min(v for v in losses.values() if not np.isnan(v)),
        max(losses.values()),
    )

    heatmap = ax1.imshow(
        data,
        cmap=cmap,
        extent=[die_x_min - 0.5, die_x_max + 0.5, die_y_min - 0.5, die_y_max + 0.5],
        origin="lower",
        vmin=vmin,
        vmax=vmax,
    )

    ax1.set_xlim(die_x_min - 0.5, die_x_max + 0.5)
    ax1.set_ylim(die_y_min - 0.5, die_y_max + 0.5)

    for (i, j), v in losses.items():
        if not np.isnan(v):
            ax1.text(
                i,
                j,
                f"{v:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=fontsize,
            )

    plt.colorbar(heatmap, ax=ax1)

    # Second subplot: Binary map based on specifications
    binary_map = np.where(
        np.isnan(data),
        np.nan,
        np.where((data >= lower_spec) & (data <= upper_spec), 1, 0),
    )

    cmap_binary = mcolors.ListedColormap(["red", "green"])
    heatmap_binary = ax2.imshow(
        binary_map,
        cmap=cmap_binary,
        extent=[die_x_min - 0.5, die_x_max + 0.5, die_y_min - 0.5, die_y_max + 0.5],
        origin="lower",
        vmin=0,
        vmax=1,
    )

    ax2.set_xlim(die_x_min - 0.5, die_x_max + 0.5)
    ax2.set_ylim(die_y_min - 0.5, die_y_max + 0.5)

    for (i, j), v in losses.items():
        if not np.isnan(v):
            ax2.text(
                i,
                j,
                f"{v:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=fontsize,
            )

    ax2.set_xlabel("Die X", fontsize=fontsize)
    ax2.set_ylabel("Die Y", fontsize=fontsize)
    ax2.set_title('KGD "Pass/Fail"', fontsize=fontsize, pad=10)
    plt.colorbar(heatmap_binary, ax=ax2, ticks=[0, 1]).set_ticklabels(
        ["Outside Spec", "Within Spec"]
    )
    return fig


def run(
    wafer_pkey: int,
    lower_spec: float,
    upper_spec: float,
    analysis_function_id: str,
    metric: str,
    key: str,
    value: float | None = None,
) -> dict[str, Any]:
    """Returns wafer map of metric after analysis_function_id.

    Args:
        wafer_pkey: pkey of the wafer to analyze.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        analysis_function_id: Name of the die function to analyze.
        metric: Metric to analyze.
        key: Key of the parameter to analyze.
        value: Value of the parameter to analyze.
    """
    device_datas = dd.get_data_by_query([dd.Wafer.pkey == wafer_pkey])

    if device_datas is None:
        raise ValueError(f"Wafer with {wafer_pkey} doesn't exist in the database.")

    dies = [data[0].die for data in device_datas]

    # Get individual die analysis results without duplicates
    die_pkeys = {die.pkey: die for die in dies}
    losses = {}

    for die in die_pkeys.values():
        losses[(die.x, die.y)] = np.nan
        for analysis in die.analysis:
            if (die.x, die.y) not in losses:
                losses[(die.x, die.y)] = np.nan
            if (
                value
                and analysis.parameters.get("key") == key
                and analysis.parameters.get("value") == value
                and analysis.analysis_function.analysis_function_id
                == analysis_function_id
            ):
                losses[(die.x, die.y)] = analysis.output[metric]

            if (
                analysis.parameters.get("key") == key
                and analysis.analysis_function.analysis_function_id
                == analysis_function_id
            ):
                losses[(die.x, die.y)] = analysis.output[metric]

    losses_list = [value for value in losses.values() if isinstance(value, int | float)]
    losses_array = np.array(losses_list)
    if np.any(np.isnan(losses_array)):
        raise ValueError(
            f"No analysis with key={key!r} and value={value} and analysis_function_id={analysis_function_id!r} found."
        )

    summary_plot = plot_wafermap(
        losses,
        value=value,
        key=key,
        lower_spec=lower_spec,
        upper_spec=upper_spec,
        metric=metric,
    )

    return dict(
        output={"losses": losses_list},
        summary_plot=summary_plot,
        wafer_pkey=wafer_pkey,
    )


if __name__ == "__main__":
    d = run(
        478, key="components", metric="component_loss", analysis_function_id="cutback"
    )
    print(d["output"]["losses"])
