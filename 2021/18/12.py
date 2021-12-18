with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

import re
import json

epattern = re.compile(r'\d+')
spattern = re.compile(r'\d{2,}')


def explode(word):
    open = 0
    for i, char in enumerate(word):
        if char == '[':
            open += 1
            if open >= 5:
                # return True at the end
                start = i +1
                eopen = 1
                for end, ec in enumerate(word[start:], start):
                    if ec == '[':
                        eopen += 1
                    elif ec == ']':
                        eopen -=1
                        if eopen == 0:
                            break
                exploded = word[start-1:end+1]
                L, _, R = exploded.strip('[]').partition(',')
                left_line = word[:start-1]
                right_line = word[end+1:]

                def l_replace(match):
                    old = int(match.group(0)[::-1])
                    old += int(L)
                    return str(old)[::-1]

                left_line = epattern.sub(l_replace, left_line[::-1], count=1)[::-1]

                def r_replace(match):
                    old = int(match.group(0))
                    old += int(R)
                    return str(old)
                right_line = epattern.sub(r_replace, right_line, count=1)

                new_line = f'{left_line}0{right_line}'
                return new_line
        elif char == ']':
            open -=1


def split(word):
    def _repl(match):
        n = int(match.group(0))
        L = n//2
        R = L if not n % 2 else L + 1
        return f'[{L},{R}]'
    return spattern.subn(_repl, word, count=1)


def add(w1, w2):
    return f'[{w1},{w2}]'

line, *lines = lines
for L in lines:
    line = add(line, L)
    splitting = exploding = True
    while exploding or splitting:
        exploding = True
        while exploding:
            exploding = explode(line)
            if exploding:
                line = exploding
        line, splitting = split(line)

L = json.loads(line)


def line_sum(_list):
    left, right = _list
    if isinstance(left, list):
        left = line_sum(left)
    if isinstance(right, list):
        right = line_sum(right)
    return left*3 + right*2

print(line_sum(L))
