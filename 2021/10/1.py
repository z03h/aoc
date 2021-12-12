with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

from collections import deque

pairs = {'[': ']', r'{': r'}', '<': '>', '(': ')'}

closing = set(pairs.values())

invalid = []

stack = deque()

for line in lines:
    for char in line:
        if char in pairs:
            stack.append(char)
            continue
        if char in closing:
            opening = stack.pop()
            if pairs[opening] != char:
                # wrong closing char
                invalid.append(char)
                break


values = {')': 3, ']': 57, '}': 1197, '>': 25137}

print(sum(values[_] for _ in invalid))
