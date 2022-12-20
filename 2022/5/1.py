
import re
from collections import deque

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

starting, data = data.split('\n\n')

def parse_input_buckets(starting_data) -> list[deque[str]]:
    *data, last_line = starting_data.split('\n')
    data.reverse()
    total_buckets = int(last_line.strip().split()[-1])
    buckets: list[deque[str]] = [deque() for _ in range(total_buckets)]

    for line in data:
        for i, index in enumerate(range(1, len(line), 4)):
            if line[index] == ' ':
                continue
            buckets[i].append(line[index])

    return buckets


def handle_movment(buckets: list[deque[str]], num_crates: int, from_index: int, to_index: int):
    from_bucket = buckets[from_index]
    to_bucket = buckets[to_index]
    for _ in range(num_crates):
        to_bucket.append(from_bucket.pop())

buckets = parse_input_buckets(starting)

pattern = re.compile(r'move (?P<num>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)')
for line in data.split('\n'):
    match = pattern.match(line)
    if not match:
        print('error', line)
        exit()
    handle_movment(buckets, int(match['num']), int(match['from'])-1, int(match['to'])-1)

print(''.join(bucket[-1] for bucket in buckets))
