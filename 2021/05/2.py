with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

from collections import Counter

grid = Counter()


def add_to_grid(i,j, x,y):
    if j == y:
        # only horizontal change
        for p in range(min(i, x), max(i, x)+1):
            grid[(p, y)] += 1
    elif i == x:
        # only vertical change
        for p in range(min(j, y), max(j, y)+1):
            grid[(x, p)] += 1
    else:
        # calc diagonal
        xstep = -1 if x < i else 1
        x_range = range(i, x + xstep, xstep)
        ystep = -1 if y < j else 1
        y_range = range(j, y + ystep, ystep)
        for _x, _y in zip(x_range, y_range):
            grid[(_x, _y)] +=1


for line in lines:
    ij, _, xy = line.partition(' -> ')
    ij = [int(_) for _ in ij.strip().split(',')]
    xy = [int(_) for _ in xy.strip().split(',')]
    add_to_grid(*ij, *xy)

print(sum(v >= 2 for v in grid.values()))
