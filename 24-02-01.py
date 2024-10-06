# Too Tall Toby 24-02-01

from build123d import *

densa = 7800 / 1e6  # carbon steel density g/mm^3
densb = 2700 / 1e6  # aluminum alloy
densc = 1020 / 1e6  # ABS

with BuildPart() as p:
    with BuildSketch() as s1:
        with BuildLine() as line:
            l_1 = Line((0, 0), (0, 105))
            RadiusArc(start_point=(0, 105), end_point=(60, 105), radius=30)
            l_2 = Line((60, 105), (60, 0))
            l_3 = Line((60, 0), (50, 0))
            l_4 = Line((50, 0), (50, 80))
            l_5 = Line((50, 80), (10, 80))
            l_6 = Line((10, 80), (10, 0))
            l_7 = Line((10, 0), (0, 0))
        make_face()
    extrude(amount=60, mode=Mode.ADD)

    with Locations(p.faces().sort_by(Axis.Z)[-1].vertices().sort_by(Axis.Y)[0]):
        with Locations((30, 105)):
            CounterSinkHole(
                radius=12.5,
                counter_sink_radius=12.5 + 5,
                counter_sink_angle=90,
            )
    with BuildSketch(p.faces().sort_by(Axis.X)[9]):
        with BuildLine():
            l_1 = Line((40, -30), (40, 30))
            RadiusArc(
                start_point=(40, 30),
                end_point=(40, -30),
                radius=30,
                short_sagitta=False,
            )
        make_face()

    extrude(amount=40, mode=Mode.ADD)

    with BuildSketch(p.faces().sort_by(Axis.X)[0]):
        with Locations((-25, 0)):
            SlotOverall(
                width=40,
                height=15,
                rotation=90,
            )

    extrude(amount=-60, mode=Mode.SUBTRACT)

    fillet(p.faces().group_by(Axis.Y)[0].edges().filter_by(Axis.X), radius=8)

    mirror(about=Plane.XY.offset(30), mode=Mode.INTERSECT)


export_step(p.part, "./models/24-02-01.step")
print(f"Part mass = {p.part.volume*densa:0.2f}")
