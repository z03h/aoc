with open('input', 'r') as f:
    data = f.read()

lines = data.split()
num = 0

import re
import functools

words = [
    'zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine',
]
valid = list('1234567890')
valid.extend(words)

digits = {w: i for i, w in enumerate(words)}

fp = re.compile(rf"{'|'.join(valid)}")
rp = re.compile(rf"{'|'.join(r[::-1] for r in valid)}")

@functools.cache
def translate(x: str) -> int:
    try:
        return int(x)
    except ValueError:
        return digits[x]

for line in lines:
    fm = fp.search(line)[0]
    rm = rp.search(line[::-1])[0][::-1]
    num += translate(fm) * 10
    num += translate(rm)

print(num)
