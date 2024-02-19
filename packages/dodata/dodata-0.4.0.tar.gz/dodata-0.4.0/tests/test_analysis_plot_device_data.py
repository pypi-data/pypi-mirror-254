import doplaydo.dodata as dd

if __name__ == "__main__":
    PROJECT_NAME = "rings"

    plots = dd.analysis.get_device_data_analysis_plots(
        project_id=PROJECT_NAME,
        device_id="rings_RingDouble-20-200-_add_fiber_array_ea36ac06_331580_243771",
        die_x=-1,
        die_y=-1,
        wafer_id='6d4c615ff105'
    )
    print(len(plots))
