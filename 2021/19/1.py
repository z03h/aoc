from itertools import permutations
from functools import cache

with open('input') as f:
    lines = f.read().split('\n\n')

lines = [L.strip().split('\n')[1:] for L in lines]
lines = [[[int(x) for x in _.split(',')] for _ in L] for L in lines]


@cache
def rotate(x, y, z):
    combos = {}
    i = 0
    for combo in [
        (x,y,z),
        (-x,y,z),
        (x,-y,z),
        (x,y,-z),
        (-x,-y,z),
        (-x,y,-z),
        (x,-y,-z),
        (-x,-y,-z),
    ]:
        for combo in permutations(combo):
            combos[i] = combo
            i += 1
    return combos


master = lines[0]
points = set(tuple(_) for _ in master)
other = set()
lines = lines[1:]

while lines:
    found = False
    line = lines.pop(0)
    print('lines', len(lines))
    for mx, my, mz in master:
        # get distance from a point
        zeroed = set((x-mx, y-my, z-mz) for x,y,z in master)
        # create all rotations
        rotations = [rotate(*P) for P in line]

        # get rotation
        for i in range(len(rotations[0])):
            coords = [r[i] for r in rotations]

            # get zeroed offsets from all coords
            for px, py, pz in coords:
                pzeroed = set((x-px, y-py, z-pz) for x,y,z in coords)
                common = zeroed & pzeroed
                if len(common) >= 12:
                    ox, oy, oz = mx-px, my-py, mz-pz
                    for x, y, z in coords:
                        point = (x+ox, y+oy, z+oz)
                        points.add(point)
                        if point not in master:
                            master.append(point)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        lines.append(line)

print(len(points))

