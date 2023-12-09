from itertools import cycle



with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

directions, data = data
lookup = {}

for line in data.splitlines():
    source, d = line.split(' = ')
    l, r = d[1:-1].split(', ')
    # print(source, l , r)
    lookup[source] = {'L': l, 'R': r}

current = 'AAA'
i = 0
for i, move in enumerate(cycle(directions), 1):
    moved = lookup[current][move]
    # print(i, move, current, moved)
    if moved == 'ZZZ':
        break
    current = moved

print(i)