


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

grid = {}
start = (-1, -1)
for rownum, row in enumerate(data):
    for colnum, char in enumerate(row):
        grid[rownum, colnum] = char
        if char == 'S':
            start = rownum, colnum


even = set()
odd = set()

valid = [start]

for step in range(65):
    if not valid:
        break

    seen = odd if step % 2 else even

    new_valid = []

    for coord in valid:
        if coord in seen:
            continue
        seen.add(coord)

        # add 4 around it
        row, col = coord
        for i in (1, -1):
            nr = row + i
            nc = col + i
            n1 = (nr, col)
            n2 = (row, nc)
            if n1 in grid and grid[n1] != '#' and n1 not in seen:
                new_valid.append(n1)
            if n2 in grid and grid[n2] != '#' and n2 not in seen:
                new_valid.append(n2)
    valid = new_valid

print(len(even), len(odd))
