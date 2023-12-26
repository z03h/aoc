from collections import Counter


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# key ... start zheight
# value ...
bricks = []
bottom_bricks = {}

for brick_id, line in enumerate(data):
    starts, _, stops = line.partition('~')
    (xs, ys, zs), (xe, ye, ze) = starts.split(','), stops.split(',')
    k = [int(_) for _ in (xs, ys, xe, ye, zs, ze, brick_id)]
    zs = int(zs)
    ze = int(ze)
    zsbricks = bottom_bricks.setdefault(zs, [])

    zsbricks.append(k)
    bricks.append(k)

bottom_bricks = {k: v for k, v in sorted(bottom_bricks.items())}
for v in bottom_bricks.values():
    v.sort()


def collide(xs1, xe1, ys1, ye1, xs2, xe2, ys2, ye2):
    return (
        (
            (xs1 <= xs2 <= xe1) or (xs1 <= xe2 <= xe1) or (xs2 <= xs1 <= xe2) or (xs2 <= xe1 <= xe2)
        ) and (
            (ys1 <= ys2 <= ye1) or (ys1 <= ye2 <= ye1) or (ys2 <= ys1 <= ye2) or (ys2 <= ye1 <= ye2)
        )
    )

fallen_bricks = {}
top_bricks = {}
# move bricks down
for k, current_bricks in bottom_bricks.items():

    for state in current_bricks:
        (xs, ys, xe, ye, zs, ze, brick_id) = state
        new_zs = -1
        for lower_z in range(zs-1, 0, -1):
            # find first brick below it that touches
            if lower_z not in top_bricks:
                continue

            for (xs2, ys2, xe2, ye2, zs2, ze2, brick_id2) in top_bricks[lower_z]:
                if collide(xs2, xe2, ys2, ye2, xs, xe, ys, ye):
                    new_zs = ze2 + 1
                    break

            if new_zs != -1:
                break

        if new_zs == -1:
            new_zs = 1

        new_ze = ze - (zs - new_zs)

        zsbricks = fallen_bricks.setdefault(new_zs, [])
        zsbricks.append((xs, ys, xe, ye, new_zs, new_ze, brick_id))

        zebricks = top_bricks.setdefault(new_ze, [])
        zebricks.append((xs, ys, xe, ye, new_zs, new_ze, brick_id))


"""
print('bottoms',list(fallen_bricks.keys()))
for k, v in fallen_bricks.items():
    print(k, v)

print('tops', list(top_bricks.keys()))
for k, v in top_bricks.items():
    print(k, v)
"""

hz = max(fallen_bricks)
hz2 = max(top_bricks)

implicit = [i[6] for i in fallen_bricks[hz]]
for i in top_bricks[hz2]:
    implicit.append(i[6])

removed = 0
cr = set()
for z_level in range(hz, 1, -1):
    # go from top down
    if z_level not in fallen_bricks:
        continue
    current_bricks = fallen_bricks[z_level]
    lower_z = z_level - 1
    lower_bricks = top_bricks[lower_z]
    can_remove = set(i[6] for i in lower_bricks)
    for cx1, cy1, cx2, cy2, cz1, cz2, cid in current_bricks:
        collisions = set()
        for lx1, ly1, lx2, ly2, lz1, lz2, lid in lower_bricks:
            if collide(cx1, cx2, cy1, cy2, lx1, lx2, ly1, ly2):
                collisions.add(lid)
                if len(collisions) > 1:
                    collisions.clear()
                    break
        can_remove = can_remove - collisions
    cr |= can_remove
    removed += len(can_remove)
print(removed, len(set(implicit)))
