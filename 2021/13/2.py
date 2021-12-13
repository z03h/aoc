with open('input') as f:
    points, folds = f.read().split('\n\n')
    points = points.split('\n')
    folds = folds.split('\n')

points = [_ for _ in points if _]
folds = [_ for _ in folds if _]

from collections import defaultdict

grid = defaultdict(dict)

for point in points:
    col, _, row = point.partition(',')
    r = int(row)
    c = int(col)
    grid[c][r] = 1

for fold in folds:
    temp_grid = defaultdict(dict)
    directions = fold.split(' ')[-1]
    orientation, _, index = directions.partition('=')
    index = int(index)
    if orientation == 'y':
        # horizontal fold
        for col, row_indexes in grid.items():
            for row, value in row_indexes.items():
                if (
                    value == 1 and
                    row > index
                ):
                    new_row = index - (row - index)
                    grid[col][row] = 0
                    temp_grid[col][new_row] = 1

    elif orientation == 'x':
        # vertical fold
        for col, row_indexes in grid.items():
            for row, value in row_indexes.items():
                if (
                    value == 1 and
                    col > index
                ):
                    new_col = index - (col - index)
                    grid[col][row] = 0
                    temp_grid[new_col][row] = 1

    for col, row_indexes in temp_grid.items():
        for row, value in row_indexes.items():
            if value:
                grid[col][row] = value

print(sum(sum(col.values()) for col in grid.values()), 'total')

max_col = max(_ for _, values in grid.items() if any(values.values()))
max_row = 0
for col, rows in grid.items():
    for row, value in rows.items():
        if value:
            if row > max_row:
                max_row = row
print(max_row)
print(max_col, max_row)

for row in range(max_row+1):
    cur_row = []
    for col in range(max_col+1):
        index = grid.get(col)
        if index:
            value = index.get(row)
            if value:
                cur_row.append('#')
                continue
        cur_row.append('.')
    print(''.join(cur_row))
