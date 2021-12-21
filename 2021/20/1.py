with open('input') as f:
    lines = f.read().split('\n\n')
algo, image = lines
_image = image.strip().split('\n')
image = {}
for row, row_line in enumerate(_image):
    for col, char in enumerate(row_line):
        image[row, col] = char

zero_val = algo[0]
max_val = algo[-1]
empty_char = '.'
active_char = '#'


# only need to update ones around #
def get_adjacent(row, col, split=False):
    if split:
        points = []
        for r in (row-1, row, row+1):
            points.append(tuple((r, c) for c in (col-1, col, col+1)))
        return (points)
    else:
        points = set()
        for r in (row-1, row, row+1):
            for c in (col-1, col, col+1):
                points.add((r, c))
        return points


def points_to_update(image):
    points = set()
    for (r, c), value in image.items():
        if value == active_char:
            points |= get_adjacent(r, c)
    return points


def update(image):
    global empty_char
    global active_char

    updated = {}
    points = points_to_update(image)
    for point in points:
        binary = []
        for bits in get_adjacent(*point, split=True):
            for bit in bits:
                binary.append(image.get(bit, empty_char))
        binary = ''.join(binary).replace('.', '0').replace('#', '1')

        binary = int(binary, 2)
        updated[point] = algo[binary]

    if empty_char == '.':
        empty_char = zero_val
    else:
        empty_char = max_val
    active_char = '.' if empty_char == '#' else '#'
    return updated


def iprint(image, other=None):
    if not other:
        minrow = min(image, key=lambda t: t[0])
        maxrow = max(image, key=lambda t: t[0])
        mincol = min(image, key=lambda t: t[1])
        maxcol = max(image, key=lambda t: t[1])
    else:
        minrow = min(other, key=lambda t: t[0])
        maxrow = max(other, key=lambda t: t[0])
        mincol = min(other, key=lambda t: t[1])
        maxcol = max(other, key=lambda t: t[1])
    for row in range(minrow[0], maxrow[0]+1):
        line = []
        for col in range(mincol[1], maxcol[1]+1):
            line.append(image.get((row,col), empty_char))
        print(''.join(line))


image = update(image)
image = update(image)

total = sum(v == '#' for v in image.values())
print(total)
