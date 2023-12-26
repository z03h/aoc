
from __future__ import annotations
from collections import namedtuple

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

    def mul(self, scalar: int):
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


def interscetion2d(vv0: tuple[Vector3D, Vector3D], vv1: tuple[Vector3D, Vector3D]) -> Vector3D | bool | None:
    a, v1 = vv0
    c, v2 = vv1
    if v1.parallel2d(v2):
        return None

    slope1 = v1.y/v1.x
    slope2 = v2.y/v2.x

    c1 = (a.y - slope1 * a.x)
    c2 = (c.y - slope2 * c.x)

    x = (c2 - c1)/(slope1-slope2)

    if v1.x < 0 and x > a.x:
        return False
    elif v1.x >= 0 and x < a.x:
        return False

    if v2.x < 0 and x > c.x:
        return False
    elif v2.x >= 0 and x < c.x:
        return False

    y = x * slope1 + c1

    inter = Vector3D(x, y, 0)

    return inter



# 13 = -1/2 * 19 + 4
# 13 = -9.5 + b
# b = 22.5?

num_i = 0

for i in range(len(vecs)):
    v0 = vecs[i]
    for v1 in vecs[i+1:]:
        inter = interscetion2d(v0, v1)
        if inter and LOWER <= inter.x <= HIGHER and LOWER <= inter.y <= HIGHER:
            num_i += 1

print(num_i)


























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