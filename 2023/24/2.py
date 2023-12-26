
from __future__ import annotations
from collections import namedtuple

from z3 import Solver, Int, Real

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

LOWER = 200000000000000
HIGHER = 400000000000000

class Vector3D:

    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def add(self, other: Vector3D):
        return Vector3D(self.x+other.x, self.y+other.y, self.z+other.z)

    def mul(self, scalar: float):
        return Vector3D(self.x*scalar, self.y*scalar, self.z*scalar)

    def parallel(self, other: Vector3D):
        return all(max(p0, p1) % min(p0, p1) == 0 for p0, p1 in zip(self, other))

    def parallel2d(self, other: Vector3D):
        return abs(self.y/self.x - other.y/other.x) < 0.0001

    def time_to_point(self, other: Vector3D) -> int:
        ...

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return f'<{self}>'

vecs: list[tuple[Vector3D, Vector3D]] = []

for line in data:
    xyz, _, direction = line.partition(' @ ')
    xyz = tuple(int(i) for i in xyz.split(','))
    direction = tuple(int(i) for i in direction.split(','))
    vecs.append((Vector3D(*xyz), Vector3D(*direction)))  # type: ignore


# what the fuck is z3
fx, fy, fz = Real("fx"), Real("fy"), Real("fz")
fdx, fdy, fdz = Real("fdx"), Real("fdy"), Real("fdz")

solver = Solver()
for idx, (xyz, direction)in enumerate(vecs[:4], 1):
    t = Real(f"t{idx}")
    x, y, z, dx, dy, dz = *xyz, *direction
    solver.add(t >= 0)
    solver.add(x + dx * t == fx + fdx * t)
    solver.add(y + dy * t == fy + fdy * t)
    solver.add(z + dz * t == fz + fdz * t)

solver.check()
solved: IntNumRef = solver.model().eval(fx + fy + fz)  # type: ignore
print(solved.as_long())































def interscetion3d(vv0: tuple[Vector3D, Vector3D], vv1: tuple[Vector3D, Vector3D]) -> Vector3D | None:
    a, v1 = vv0
    c, v2 = vv1
    print(a, v1)
    print(c, v2)

    if v1.parallel(v2):
        return None

    top = ((c.x-a.x)* -v2.y) - ((c.y - a.y) * -v2.y)
    bottom = (v1.x * -v2.y) - (v1.y * -v2.x)

    inter = a.add(v1.mul(top/bottom))
    print(inter)

    return inter