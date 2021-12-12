with open('input') as f:
    lines = f.read().split('\n')
lines = [[int(i) for i in _] for _ in lines if _]


def _print(day=None):
    print('day', day)
    print('\n'.join(' '.join(str(i) for i in _) for _ in lines))


def get_adjacent(i, j, flashed):
    for row in (i-1, i, i+1):
        for col in (j-1, j, j+1):
            if (
                (row == i and col == j) or
                (row, col) in flashed or
                row < 0 or
                row >= len(lines) or
                col < 0 or
                col >= len(lines[0])
            ):
                continue
            yield row, col


def flash(i, j, flashed):
    if (i, j) in flashed:
        return flashed
    flashed.add((i, j))
    for row, col in get_adjacent(i, j, flashed):
        lines[row][col] += 1
        if lines[row][col] > 9:
            flashed = flash(row, col, flashed)
    return flashed


total_flashes = 0

for _ in range(100):
    flashed = set()
    # increment all by 1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] += 1

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > 9:
                flashed = flash(i, j, flashed)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > 9:
                lines[i][j] = 0

    total_flashes += len(flashed)
_print(_+1)
print('=', total_flashes, '\n')

