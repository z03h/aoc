import string
import itertools

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

letter_lookup = {}

for i, char in enumerate(string.ascii_letters, 1):
    letter_lookup[char] = i

priorities = 0

def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


for group in grouper(3, data.split('\n')):
    char = next(iter(set(group[0]) & set(group[1]) & set(group[2])))
    priorities += letter_lookup[char]

print(priorities)

