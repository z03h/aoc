with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]


fuck = 'def run(s):\n    w = x = y = z = i= 0\n    '


def parse(line):
    action, *nums = line.split()
    if action == 'inp':
        return f'{nums[0]} = int(s[i])\n    i += 1'
    elif action == 'add':
        c1 = nums[0]
        c2 = nums[1]
        return f'{c1} += {c2}'
    elif action == 'mul':
        c1 = nums[0]
        c2 = nums[1]
        return f'{c1} *= {c2}'
    elif action == 'div':
        c1 = nums[0]
        c2 = nums[1]
        return f'{c1} //= {c2}'
    elif action == 'mod':
        c1 = nums[0]
        c2 = nums[1]
        return f'{c1} %= {c2}'
    elif action == 'eql':
        c1 = nums[0]
        c2 = nums[1]
        return f'{c1} = {c1} == {c2}'


to_add = []

for line in lines:
    to_add.append(parse(line))

file = fuck + '\n    '.join(to_add)
with open('helper.py', 'w') as f:
    f.write(file)
    f.write('\n    return z')

from helper import run

for i in range(99999999999999, -1, -1):
    if not i % 100_000:
        print(i)
    i = str(i)
    if '0' in i:
        continue
    z = run(i)
    if z == 0:
        print(i)
        break

