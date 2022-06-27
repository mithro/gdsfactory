"""When you create components you have to make sure they have unique names.

the cell decorator gives unique names to components that depend on their parameters
"""

import gdsfactory as gf
from gdsfactory.types import LayerSpec


@gf.cell
def straight(
    length: float = 5.0, width: float = 1.0, layer: LayerSpec = (2, 0)
) -> gf.Component:
    """Returns straight Component.

    Args:
        length: of the straight.
        width: in um.
        layer: layer spec
    """
    wg = gf.Component("straight_sample")
    wg.add_polygon([(0, 0), (length, 0), (length, width), (0, width)], layer=layer)
    wg.add_port(
        name="o1", midpoint=(0, width / 2), width=width, orientation=180, layer=layer
    )
    wg.add_port(
        name="o2", midpoint=(length, width / 2), width=width, orientation=0, layer=layer
    )
    return wg


def test_autoname() -> None:
    c1 = straight(length=5)
    assert c1.name.split("_")[0] == "straight"


if __name__ == "__main__":
    c1 = straight(length=5)
    print(c1)
    c1.show()
