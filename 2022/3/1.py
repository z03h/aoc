import string

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

letter_lookup = {}

for i, char in enumerate(string.ascii_letters, 1):
    letter_lookup[char] = i

priorities = 0

for line in data.split('\n'):
    half = len(line)//2
    first = line[:half]
    second = line[half:]
    char = next(iter(set(first) & set(second)))
    priorities += letter_lookup[char]

print(priorities)

