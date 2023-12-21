
from collections import deque


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

modules = {}
reverse_modules = {'broadcaster': []}
# Flip-flop modules (prefix %) are either on or off; they are initially off.
# If a flip-flop module receives a high pulse, it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse, it flips between on and off.
# If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules;
# they initially default to remembering a low pulse for each input.
# When a pulse is received, the conjunction module first updates its memory for that input.
# Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

for line in data:
    name, _, output = line.partition(' -> ')
    if name == 'broadcaster':
        modules[name] = None, None, list(map(str.strip, output.split(',')))
    else:
        mtype = name[0]
        name = name[1:]
        if mtype == '%':
            # flip flop
            state = False
        elif mtype == '&':
            # conjuction
            state = {}
        else:
            raise ValueError('huh ' + mtype)
        modules[name] = mtype, state, list(map(str.strip, output.split(',')))

    for o in modules[name][2]:
        reverse_modules.setdefault(o, []).append(name)



all_conjuc = list(mname for mname, k in modules.items() if k[0] == '&')

for conj in all_conjuc:
    _, state, _ = modules[conj]

    for othername, (_, _, output) in modules.items():
        if conj in output:
            state[othername] = False
"""
f = open('mermaid.txt', 'w+')
f.write('flowchart TD\n')

nodes = deque()
nodes.append('broadcaster')
seen = set()
seen.add('rx')
names = {name: (hex(i), _[0]) for i, (name, _) in enumerate(modules.items())}
names['rx'] = 'ZZ', None

while nodes:
    m = nodes.popleft()
    if m in seen:
        continue
    seen.add(m)
    _, _, outputs = modules[m]
    src, stype = names[m]
    for o in outputs:
        nodes.append(o)
        dest, dtype = names[o]
        f.write(f'    {src}[{stype}{m}] --> {dest}[{dtype}{o}]\n')


f.close()
"""








def get_state(modules):
    new_state = {}
    for mname, (mtype, state, _) in modules.items():
        if mtype == '%':
            # flip
            new_state[mname] = state
        elif mtype == '&':
            # conjunction
            new_state[mname] = state.copy()
        else:
            # ???
            raise ValueError('invalid mtype')

    return new_state




button_count = 0
care = {}

while 1:
    #current_state = get_state(modules)

    #pulses = [1 + len(start), 0] # low, high pulse counts
    button_count += 1
    queue = deque()
    for mod in modules['broadcaster'][2]:
        queue.append(('broadcaster', False, mod))
    if not button_count % 5000000:
        print('presses', f'{button_count:,}', care)

    while queue:
        source, pulse, module_name = queue.popleft()
        if module_name == 'qb' and pulse:
            care[source] = button_count
            if len(care) == 4:
                import math
                print(care, math.lcm(*care.values()))
                exit()

        #print(source, int(pulse), module_name)
        module = modules.get(module_name)

        if not module:
            # print('module not found, what do?', module_name)
            continue
        mtype, state, outputs = module

        match mtype, pulse:
            case '%', False:
                # flip-flop sent low, flip state on off
                state = not state
                out = state

            case '&', False:
                # conj got sent a low
                state[source] = False
                out = True
            case '&', True:
                # conj got sent high
                state[source] = True
                out = not all(state.values())
            case _, _:
                # flip flip
                continue

        modules[module_name] = mtype, state, outputs


        for output in outputs:
            #pulses[out] += 1
            queue.append((module_name, out, output))

    #print('-'*10)

    #states.append(current_state)
    #pulse_counts.append(pulses)



