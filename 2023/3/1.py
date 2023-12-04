

with open('input.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')

import re

pattern = re.compile(r'[^\.0-9]')
numbers = re.compile(r'[0-9]+')

found_numbers = []
total = 0

for line in lines:
    found_numbers.append(list(numbers.finditer(line)))


def inside(m: re.Match, start: int, mid: int, end: int) -> bool:
    lower, higher = m.start(), m.end()-1
    return (
        start <= lower <= end or
        start <= higher <= end or
        lower <= mid <= higher
    )


for row, line in enumerate(lines):
    matches = list(pattern.finditer(line))

    if not matches:
        continue

    for symbol in matches:
        mid, end = symbol.start(), symbol.end()
        start = mid - 1

        if row-1 >= 0 :
            above = found_numbers[row-1]
            for number in above:
                if inside(number, start, mid, end):
                    total += int(number[0])

        current = found_numbers[row]
        for number in current:
            if number.end() == mid or number.start() == end:
                total += int(number[0])

        if row+1 < len(lines):
            above = found_numbers[row+1]
            for number in above:
                if inside(number, start, mid, end):
                    total += int(number[0])

print(total)






