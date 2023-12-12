


with open('test2.txt', 'r') as f:
    data = f.read()

empty_rows = []
empty_cols = []



data = [list(d) for d in data.splitlines()]

for rownum, row in enumerate(data):
    if all(c == '.' for c in row):
        empty_rows.append(rownum)

for colnum in range(len(data[0])):
    if all(row[colnum] == '.' for row in data):
        empty_cols.append(colnum)

galaxy = [''.join(row) for row in data]

print('\n'.join(galaxy))

stars = []

for rownum, row in enumerate(galaxy):
    for colnum, char in enumerate(row):
        if char == '#':
            # star
            stars.append((rownum, colnum))

dist = 0
c = 0
MODIFIER = 1_000_000

for index, s1 in enumerate(stars):
    for index2, s2 in enumerate(stars[index:]):
        if s1 == s2:
            continue
        c += 1
        r1, c1 = s1
        r2, c2 = s2

        lower_r, higher_r = min(r1, r2), max(r1, r2)
        lower_c, higher_c = min(c1, c2), max(c1, c2)

        crossed_row = sum(1 for cr in empty_rows if lower_r < cr < higher_r)
        crossed_col = sum(1 for cc in empty_cols if lower_c < cc < higher_c)

        #print(s1, index+1, s2, index+index2+1, '|', abs(r1 - r2), abs(c1 - c2))
        dist += (higher_r - lower_r - crossed_row + crossed_row*MODIFIER)
        dist += (higher_c - lower_c - crossed_col + crossed_col*MODIFIER)

print(c, dist)