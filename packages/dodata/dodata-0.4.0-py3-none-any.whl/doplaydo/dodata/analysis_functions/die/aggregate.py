"""Calculates device analysis mean and standard deviation."""
from typing import Any
import numpy as np
from matplotlib import pyplot as plt
import doplaydo.dodata as dd


def run(
    die_pkey: int,
    device_analysis_function: str,
    metric: str,
    device_attributes: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Returns mean and standard deviation over a die for a particular device analysis function.

    Args:
        die_pkey: pkey of the die to analyze.
        device_analysis_function: name of the device analysis function to run.
        metric: metric to return from the device analysis function and to calculate mean and std over.
        device_attributes: settings to filter devices by.
    """
    device_attributes = device_attributes or {}

    analyses = dd.db.analysis.get_analyses_for_die_by_pkey(
        die_pkey=die_pkey,
        target_model="device_data",
        filter_clauses=[
            dd.attribute_filter(dd.Cell, key, value)
            for key, value in device_attributes.items()
        ],
    )

    values = []
    device_ids = []

    for analysis in analyses:
        device_ids.append(analysis.device_data.device.device_id)
        values.append(analysis.output[metric])
        if not isinstance(analysis.output[metric], float | int):
            raise ValueError(
                f"Analysis output {analysis.output[metric]} is not a float or int"
            )

    if not values:
        raise ValueError(
            f"No analysis data found for die_pkey {die_pkey}, {device_attributes}, "
            f"device_analysis_function = {device_analysis_function!r}, metric = {metric!r}"
        )

    fig = plt.figure()
    plt.plot(device_ids, values, "o")
    plt.xlabel("Device name")
    plt.ylabel(metric)
    plt.title(f"{metric} for die {die_pkey}")

    return dict(
        output={
            "mean": np.mean(values),
            "std": np.std(values),
            "median": np.median(values),
        },
        summary_plot=fig,
        die_pkey=die_pkey,
    )


if __name__ == "__main__":
    d = run(
        309,
        device_analysis_function="device_fsr",
        metric="fsr_mean",
        device_attributes={"radius_um": 10, "gap_um": 0.2},
    )
    print(d["output"]["mean"])
