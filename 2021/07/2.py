with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]
line = [int(_) for _ in lines[0].split(',')]

min_value = min(line)
max_value = max(line)

import functools


@functools.cache
def range_sum(i):
    return int(i * (i + 1)/2)


print(min(sum(range_sum(abs(_ - i)) for i in line) for _ in range(min_value, max_value+1)))
