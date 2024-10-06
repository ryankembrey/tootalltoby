# Too Tall Toby 24-01-04

from build123d import *

densa = 7800 / 1e6  # carbon steel density g/mm^3
densb = 2700 / 1e6  # aluminum alloy
densc = 1020 / 1e6  # ABS

with BuildPart() as p:
    with BuildSketch(Plane.XZ) as s1:
        RectangleRounded(98, 64, radius=20)
        with Locations((-1, 0)):
            RectangleRounded(98 - 2 * 15, 64 - 16 * 2, radius=7, mode=Mode.SUBTRACT)
    extrude(amount=18)

    split(bisect_by=Plane.XY, keep=Keep.BOTTOM)

    with BuildSketch(p.faces().sort_by(Axis.X)[-1]) as s2:
        with Locations((12 / 2, 0)):
            Circle(radius=18 / 2)
    extrude(amount=-16)

    with BuildSketch(p.faces().sort_by(Axis.X)[3]) as s3:
        with Locations((9 / 2, 0)):
            Circle(radius=18 / 2, mode=Mode.ADD)

    extrude(amount=-25)

    with BuildSketch(p.faces().sort_by(Axis.X)[0]) as s4:
        Circle(radius=4)
    extrude(amount=-25, mode=Mode.SUBTRACT)

export_step(p.part, "24-01-04.step")
print(f"Part mass = {p.part.volume*densa:0.2f}")
