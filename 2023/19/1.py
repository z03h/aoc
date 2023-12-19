

from collections import namedtuple
import re


Part = namedtuple('Part', ('x', 'm', 'a', 's'))

with open('input.txt', 'r') as f:
    data = f.read()

sworkflows, sparts = data.split('\n\n')
sworkflows = sworkflows.splitlines()
sparts = sparts.splitlines()

parts: list[dict] = [eval(f'dict({line[1:-1]})') for line in sparts]

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


workflows = {}
for line in sworkflows:
    wf = WF(line)
    workflows[wf.name] = wf

val = 0
for part in parts:
    flow = workflows['in']
    while True:
        next_flow = flow.match(part)
        if next_flow == 'A':
            val += sum(part.values())
            break
        elif next_flow == 'R':
            break

        flow = workflows[next_flow]

print(val)



