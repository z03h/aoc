


with open('input.txt', 'r') as f:
    data = f.read()

empty_rows = []



data = [list(d) for d in data.splitlines()]

for rownum, row in enumerate(data):
    if all(c == '.' for c in row):
        empty_rows.append(rownum)

for colnum in range(len(data[0])):
    if all(row[colnum] == '.' for row in data):
        for row in data:
            row[colnum] = '..'

galaxy = [''.join(row) for row in data]

for index in reversed(empty_rows):
    galaxy.insert(index, '.' * len(galaxy[0]))

print('\n'.join(galaxy))

stars = []

for rownum, row in enumerate(galaxy):
    for colnum, char in enumerate(row):
        if char == '#':
            # star
            stars.append((rownum, colnum))

dist = 0
c = 0
for index, s1 in enumerate(stars):
    for index2, s2 in enumerate(stars[index:]):
        if s1 == s2:
            continue
        c += 1
        r1, c1 = s1
        r2, c2 = s2
        #print(s1, index+1, s2, index+index2+1, '|', abs(r1 - r2), abs(c1 - c2))
        dist += abs(r1 - r2) + abs(c1 - c2)

print(c, dist)