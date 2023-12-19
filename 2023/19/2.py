

from collections import namedtuple, deque
import re


Part = namedtuple('Part', ('x', 'm', 'a', 's'))

with open('input.txt', 'r') as f:
    data = f.read()

sworkflows, sparts = data.split('\n\n')
sworkflows = sworkflows.splitlines()
sparts = sparts.splitlines()

# parts: list[dict] = [eval(f'dict({line[1:-1]})') for line in sparts]

c_pattern = re.compile(r'(.)([\<\>])([0-9]+):(.+)')

class WF:
    def __init__(self, line: str):
        self.name, _, conditions = line.partition(r'{')
        _conds = conditions[:-1].split(',')
        self.conditions = []
        self.last_cond = _conds[-1]
        for c in _conds[:-1]:
            match = c_pattern.match(c)
            if match:
                # condition jump
                cond = tuple(match[i] for i in range(1, 5))
            else:
                # just jump
                cond = c

            self.conditions.append(cond)

    def match(self, part: dict) -> bool | str:
        for cond in self.conditions:
            attr, comp, value, result = cond
            value = int(value)
            if comp == '<':
                if part[attr] < value:
                    return result
            elif comp == '>':
                if part[attr] > value:
                    return result

        return self.last_cond


    def range_match(self, r: dict[str, range]):
        new_ranges = []
        current = r
        cont = None
        for cond in self.conditions:
            attr, comp, value, result = cond
            value = int(value)
            attr_range: range = current[attr]
            start, stop = attr_range.start, attr_range.stop

            if comp == '<':
                done = range(start, min(stop, value-1))
                cont = range(max(start, value), stop)
            elif comp == '>':
                cont = range(start, min(stop, value))
                done = range(max(start, value+1), stop)

            new_r = r.copy()
            new_r[attr] = done
            new_ranges.append((result, new_r))
            current[attr] = cont
            #print('####', new_r[attr], current[attr])

        new_ranges.append((self.last_cond, current))

        return new_ranges


workflows = {}
for line in sworkflows:
    wf = WF(line)
    workflows[wf.name] = wf



queue = deque()
queue.append(('in', {c: range(1, 4000) for c in 'xmas'}))

val = 0
while queue:
    name, r = queue.popleft()
    if not all(r.values()):
        continue
    if name == 'A':
        #print('+++ ACCEPT', r)
        _v = 1
        for rr in r.values():
            l, h = rr.start, rr.stop
            _v *= (h-l)+1

        val += _v
        continue
    elif name == 'R':
        #print('--- REJECT', r)
        continue

    wf = workflows[name]
    x = wf.range_match(r)
    for c in x:
        queue.append(c)

print(val)

# 167,409,079,868,000
