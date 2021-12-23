from itertools import product

with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

lines = [_.split() for _ in lines]


def split(input):
    x, y, z = input.split(',')
    x = [int(_) for _ in x[2:].split('..')]
    y = [int(_) for _ in y[2:].split('..')]
    z = [int(_) for _ in z[2:].split('..')]
    return x, y, z

points = set()

for status, coords in lines:
    x, y, z = split(coords)
    if any(_[0] > 50 or _[1] < -50 for _ in (x, y, z)):
        continue
    p = product(range(x[0], x[1]+1), range(y[0], y[1]+1), range(z[0], z[1]+1))
    if status == 'on':
        points = points.union(p)
    else:
        points = points.difference(p)
    print(len(points))

