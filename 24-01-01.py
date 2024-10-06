from build123d import *

densa = 7800 / 1e6  # carbon steel density g/mm^3
densb = 2700 / 1e6  # aluminum alloy
densc = 1020 / 1e6  # ABS

with BuildPart() as p:
    with BuildSketch() as s1:
        with BuildLine() as line:
            l_1 = Line((0, 0), (65 - 14.5, 0))
            l_2 = Line((0, 0), (0, 29))
            l_1 = Line((0, 29), (65 - 14.5, 29))
            RadiusArc((65 - 14.5, 29), (65 - 14.5, 0), 14.5)
        make_face()
    extrude(amount=15)

    with BuildSketch(p.faces().sort_by(Axis.Z)[-1]) as s2:
        with Locations((-62 / 2 + 30 / 2, 0)):
            Rectangle(30, 29)
    extrude(amount=62 - 15)

print(f"Part mass = {p.part.volume*densc:0.2f}")
export_step(p.part, "24-01-01.step")
