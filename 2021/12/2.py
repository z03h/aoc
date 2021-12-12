with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

import string
from collections import Counter, defaultdict

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
        visited = Counter()

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
            if any(v >1 for v in visited.values()) and connects in visited:
                continue
            else:
                temp.append(connects)
                temp_visit = visited.copy()
                temp_visit[connects] += 1

                sub_paths = get_paths(connects, temp, temp_visit)
        else:
            temp.append(connects)
            sub_paths = get_paths(connects, temp, visited)

        current_paths = current_paths.union(sub_paths)

    return current_paths


print(len(get_paths('start')))
