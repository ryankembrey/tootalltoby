# Too Tall Toby 24-04-02

from build123d import *
import numpy as np

densa = 7800 / 1e6  # carbon steel density g/mm^3
densb = 2700 / 1e6  # aluminum alloy
densc = 1020 / 1e6  # ABS

with BuildPart() as p:
    with BuildSketch() as s:
        Rectangle(115, 50)
        with Locations((5 / 2, 0)):
            SlotOverall(90, 12, mode=Mode.SUBTRACT)

    base = extrude(amount=15)

    with BuildSketch(Plane.XZ.offset(50 / 2)) as s2:
        with Locations((-115 / 2 + 26, 0)):
            SlotOverall(2 * 42 + 2 * 26, 26 * 2, rotation=90)

    zz = extrude(amount=-12)
    split(bisect_by=Plane.XY)

    edge1 = p.part.edges().filter_by(Axis.Y)[5]
    fillet(edge1, radius=9)

    with Locations(zz.faces().sort_by(Axis.Y)[0]):
        with Locations((26 + 15, 0)):
            CounterBoreHole(radius=12, counter_bore_radius=34 / 2, counter_bore_depth=4)

    mirror(about=Plane.XZ)

    with BuildSketch(base.faces().sort_by(Axis.X)[-1]) as s4:
        with Locations((0, -7.5 + 8 / 2)):
            Trapezoid(
                width=18 + 2 * 8 * np.tan(30 * np.pi / 180),
                height=8,
                left_side_angle=60,
                rotation=180,
            )

    extrude(amount=-115, mode=Mode.SUBTRACT)

    with BuildSketch() as s5:
        RectangleRounded(115, 50, 6)
    extrude(amount=80, mode=Mode.INTERSECT)


export_step(p.part, "24-04-02.step")
print(f"Part mass = {p.part.volume*densa:0.2f}")
