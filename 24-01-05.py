# Too Tall Toby 24-01-05

from build123d import *

densa = 7800 / 1e6  # carbon steel density g/mm^3
densb = 2700 / 1e6  # aluminum alloy
densc = 1020 / 1e6  # ABS

with BuildPart() as p:
    with BuildSketch() as s1:
        Circle(radius=4 / 2)
    extrude(amount=0.5)
    with BuildSketch() as s2:
        Circle(radius=1)
    extrude(amount=3)

    with BuildSketch(p.faces().sort_by(Axis.Z)[2]) as s3:
        spots = RegularPolygon(
            radius=1.5,
            side_count=4,
            rotation=45,
            mode=Mode.PRIVATE,
        )
        with Locations(spots.vertices()):
            Rectangle(0.5, 0.5, rotation=45)
    extrude(amount=0.5)

    with BuildSketch(p.faces().sort_by(Axis.Z)[2]) as s3:
        with Locations((1.5, 0), (0, 1.5), (0, -1.5), (-1.5, 0)):
            Rectangle(0.5, 0.5)
    extrude(amount=0.5)

    with BuildSketch() as s4:
        with Locations(p.faces().group_by(Axis.Z)[4]):
            Circle(0.25 / 2)
    extrude(amount=3)

    with BuildSketch(p.faces().sort_by(Axis.Z)[-9]) as s5:
        Circle(radius=2)
    extrude(amount=6.25 - 3)

    chamfer(p.edges().sort_by(Axis.Z)[-1], angle=30, length=2.25)

    with BuildSketch(p.faces().sort_by(Axis.Z)[-1]):
        Circle(radius=0.75 / 2)
    extrude(amount=-4.25, mode=Mode.SUBTRACT)

    with BuildSketch(p.faces().sort_by(Axis.Z)[0]):
        Circle(radius=0.75)
    extrude(amount=-2, mode=Mode.SUBTRACT)


export_step(p.part, "24-01-05.step")
print(f"Part mass = {p.part.volume*16387.064*0.002204623*densa:0.2f}")
