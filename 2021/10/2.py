with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

from collections import deque

pairs = {'[': ']', r'{': r'}', '<': '>', '(': ')'}

closing = set(pairs.values())

invalid = set()

incomplete = []

for line in lines:
    stack = deque()
    add = True
    for char in line:
        if char in pairs:
            stack.append(char)
            continue
        if char in closing:
            opening = stack.pop()
            if pairs[opening] != char:
                # wrong closing char
                invalid.add(line)
                add = False
                break
    if add:
        temp = []
        for _ in reversed(stack):
            temp.append(pairs[_])
        incomplete.append(temp)

values = {')': 1, ']': 2, '}': 3, '>': 4}

final = []
for word in incomplete:
    total = 0
    for char in word:
        total *= 5
        total += values[char]
    final.append(total)

final = sorted(final)

print(final[int((len(final)-1)/2)])
