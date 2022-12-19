
with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

horis = []
vertis = []
hfilled = {}
vfilled = {}
MAX_COL = len(lines[0])
MAX_ROW = len(lines)

for row, line in enumerate(lines):
    for col, cucumber in enumerate(line):
        pos = None
        L = None
        if cucumber == 'v':
            # verti
            pos = (row, col)
            L = vertis
            filled = vfilled
        elif cucumber == '>':
            pos = (row, col)
            L = horis
            filled = hfilled

        if pos:
            L.append(pos)
            filled[pos] = True


def move_hori(horis):
    new_hori = []
    new_filled = {}
    changed = False
    for hori in horis:
        row, col = hori
        new_col = (col + 1) % MAX_COL
        if not hfilled.get((row, new_col)) and not vfilled.get((row, new_col)):
            # move
            changed = True
            point = (row, new_col)
        else:
            point = (row, col)

        new_hori.append(point)
        new_filled[point] = True

    return new_hori, new_filled, changed


def move_verti(vertis):
    new_verti = []
    new_filled = {}
    changed = False
    for verti in vertis:
        row, col = verti
        new_row = (row + 1) % MAX_ROW
        if not hfilled.get((new_row, col)) and not vfilled.get((new_row, col)):
            # spot empty
            changed = True
            point = (new_row, col)
        else:
            point = (row, col)

        new_verti.append(point)
        new_filled[point] = True
    return new_verti, new_filled, changed


def print_board():
    for row in range(MAX_ROW):
        row_text = []
        for col in range(MAX_COL):
            if hfilled.get((row, col)):
                char = '>'
            elif vfilled.get((row,col)):
                char = 'v'
            else:
                char = '.'

            row_text.append(char)
        print(''.join(row_text))
    print()


turns = 0
while True:
    turns += 1
    horis, hfilled, hc = move_hori(horis)
    vertis, vfilled, vc = move_verti(vertis)
    if not hc and not vc:
        break

print(turns)


