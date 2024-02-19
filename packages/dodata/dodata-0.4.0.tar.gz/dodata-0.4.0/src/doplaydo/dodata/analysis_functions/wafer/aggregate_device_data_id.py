"""Aggregate analysis."""

from typing import Any
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

import doplaydo.dodata as dd
from collections import defaultdict


def plot_wafermap(
    result: dict[tuple[int, int], float],
    device_id: str,
    lower_spec: float,
    upper_spec: float,
    metric: str,
) -> Figure:
    """Plot a wafermap of the result.

    Args:
        result: Dictionary of result.
        device_id: Name of the device to analyze.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        metric: Metric to analyze.
    """
    fontsize = 16

    # Calculate the bounds and center of the data
    if not result:
        raise ValueError("No data to plot")
    die_xs, die_ys = zip(*result.keys())
    die_x_min, die_x_max = min(die_xs), max(die_xs)
    die_y_min, die_y_max = min(die_ys), max(die_ys)

    # Create the data array
    data = np.full((die_y_max - die_y_min + 1, die_x_max - die_x_min + 1), np.nan)
    for (i, j), v in result.items():
        data[j - die_y_min, i - die_x_min] = v

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.8))

    # First subplot: Heatmap
    ax1.set_xlabel("Die X", fontsize=fontsize)
    ax1.set_ylabel("Die Y", fontsize=fontsize)
    title = f"{metric} {device_id}"
    ax1.set_title(title, fontsize=fontsize, pad=10)

    cmap = plt.get_cmap("viridis")
    vmin, vmax = (
        min(v for v in result.values() if not np.isnan(v)),
        max(result.values()),
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

    for (i, j), v in result.items():
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

    for (i, j), v in result.items():
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
    device_id: str,
    lower_spec: float,
    upper_spec: float,
    analysis_function_id: str,
    metric: str,
) -> dict[str, Any]:
    """Returns wafer map of metric after analysis_function_id.

    Args:
        wafer_pkey: pkey of the wafer to analyze.
        device_id: Name of the device to analyze.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        analysis_function_id: Name of the die function to analyze.
        metric: Metric to analyze.
    """
    analyses = dd.db.analysis.get_analyses_for_wafer_by_pkey(
        wafer_pkey=wafer_pkey,
        target_model="device_data",
        filter_clauses=[
            dd.AnalysisFunction.analysis_function_id == analysis_function_id,
            dd.Device.device_id == device_id,
        ],
    )

    analyses_per_die: dict[tuple[int, int], list[dd.Analysis]] = defaultdict(list)

    for analysis in analyses:
        analyses_per_die[
            (analysis.device_data.die.x, analysis.device_data.die.y)
        ].append(analysis)

    result: dict[tuple[int, int], dd.Analysis] = {}
    for coord, analyses in analyses_per_die.items():
        max_analysis_index = np.argmax([a.pkey for a in analyses])
        last_analysis = analyses[max_analysis_index]
        o = last_analysis.output[metric]  # get the last analysis (most recent)
        if not isinstance(o, float | int):
            raise ValueError(f"Analysis output {o} is not a float or int")
        result[coord] = o

    result_list = [value for value in result.values() if isinstance(value, int | float)]
    result_array = np.array(result_list)
    if np.any(np.isnan(result_array)) or not result:
        raise ValueError(
            f"No analysis for {wafer_pkey=} {analysis_function_id=}, {device_id=}  found."
        )

    summary_plot = plot_wafermap(
        result=result,
        device_id=device_id,
        lower_spec=lower_spec,
        upper_spec=upper_spec,
        metric=metric,
    )

    return dict(
        output={"result": result_list},
        summary_plot=summary_plot,
        wafer_pkey=wafer_pkey,
    )


if __name__ == "__main__":
    # d = run(478, key="components", metric="component_loss", analysis_function_id="cutback")
    # print(d["output"]["result"])
    d = run(
        11,
        analysis_function_id="device_fsr",
        device_id="rings_RingDouble-10-0.1-_331480_776211",
    )
    print(d["output"]["result"])
