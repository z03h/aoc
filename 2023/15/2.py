
from functools import cache
from collections import defaultdict



with open('input.txt', 'r') as f:
    data = f.read()

boxes = defaultdict(defaultdict)

@cache
def tohash(chars: str) -> int:
    isum = 0
    for char in chars:
        isum += ord(char)
        isum *= 17
        isum %= 256

    return isum




for h in data.split(','):
    if h[-1] == '-':
        # remove from box
        chars = h[:-1]
        boxnum = tohash(chars)
        boxes[boxnum].pop(chars, None)

    elif h[-2] == '=':
        # set into box
        chars, _, val = h.partition('=')
        val = int(val)
        boxnum = tohash(chars)
        boxes[boxnum][chars] = val

sum = 0
for boxnum, box in boxes.items():
    for i, (char, v) in enumerate(box.items(), 1):
        #print(char, boxnum, i, v)
        sum += (boxnum+1) * i * v
print(sum)

