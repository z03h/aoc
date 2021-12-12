with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

import string
from collections import defaultdict

paths = defaultdict(set)

for line in lines:
    start, _, end = line.partition('-')
    if start != 'end' and end != 'start':
        paths[start].add(end)
    if start != 'start' and end != 'end':
        paths[end].add(start)

small = set(string.ascii_lowercase)
end_paths = []


def get_paths(point, input=None, visited=None):
    if input is None:
        input = [point]
    if visited is None:
        visited = set()
    temp_visit = visited.copy()

    current_paths = set()
    for connects in paths[point]:
        if connects == 'start':
            continue

        temp = input.copy()
        if connects == 'end':
            temp.append(connects)
            current_paths.add(tuple(temp))
            continue

        if all(c in small for c in connects):
            if connects in temp_visit:
                continue
            else:
                temp.append(connects)
                sub_paths = get_paths(connects, temp, temp_visit.union({connects}))
        else:
            temp.append(connects)
            sub_paths = get_paths(connects, temp, temp_visit)

        current_paths = current_paths.union(sub_paths)

    return current_paths

print(len(get_paths('start')))
