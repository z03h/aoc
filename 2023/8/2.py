from itertools import cycle



with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

directions, data = data
lookup = {}
starting = {}

for line in data.splitlines():
    source, d = line.split(' = ')
    if source.endswith('A'):
        starting[source] = -1
    l, r = d[1:-1].split(', ')
    # print(source, l , r)
    lookup[source] = {'L': l, 'R': r}

for current in starting:
    original = current
    i = 0
    for i, move in enumerate(cycle(directions), 1):
        moved = lookup[current][move]
        # print(i, move, current, moved)
        if moved.endswith('Z'):
            break
        current = moved

    starting[original] = i

print(' '.join(str(x) for x in starting.values()))
print(len(directions))
for v in starting.values():
    print(v, divmod(v, len(directions)))


import math
print(math.lcm(*starting.values()))
# get lcm of these values
# i guessed that each starter reaches a unique end z and not any other ever
# and loops immediately after the z