"""Generates a layout for a chip with a cutback sweep."""
from functools import partial
import pandas as pd
import gdsfactory as gf


size = (6050, 4100)
pack = partial(gf.pack, max_size=size, add_ports_prefix=False, spacing=2)
add_gc = gf.routing.add_fiber_array
ring_double = gf.components.cutback_loss_mmi1x2


@gf.cell
def cutback() -> gf.Component:
    """Returns a component cutback sweep."""
    cutback_sweep = gf.components.cutback_loss_mmi1x2(
        component=gf.components.mmi1x2(),
        loss=(0, 1, 2),
        decorator=gf.routing.add_fiber_array,
    )
    c = pack(cutback_sweep)
    if len(c) > 1:
        print(f"Failed to pack in 1 component of {size}, got {len(c)}")
        c = gf.grid(c)
    else:
        c = c[0]
    return c


@gf.cell
def top() -> gf.Component:
    """Returns a top cell."""
    c = gf.Component()
    ref = c << cutback()
    c.add_ports(ref.ports)
    return c


def write_settings_table() -> pd.DataFrame:
    """Write settings table."""
    settings = ["components"]
    c = cutback()
    references = c.get_dependencies()
    rows = []
    for r in references:
        d = dict(cell=r.name)
        for s in settings:
            d[s] = r.info.get(s, None)
        rows.append(d)

    return pd.DataFrame(rows)


if __name__ == "__main__":
    from gdsfactory.labels import get_test_manifest

    c = top()
    c.write_gds("test_chip.gds")
    df = get_test_manifest(c, one_setting_per_column=True)
    df.to_csv("test_manifest.csv", index=False)
    print(df)
    # print(df.cell_settings[0])
    # df = write_settings_table()
    # df.to_csv("cell_table.csv", index=False)
    c.show()
