from collections import deque

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


all_nodes = set()
nodes: dict[str, set[str]] = {}

for line in data:
    first, _, rest = line.partition(': ')
    rest = rest.split()
    ns = nodes.setdefault(first, set())
    all_nodes.add(first)
    for n in rest:
        nns = nodes.setdefault(n, set())
        nns.add(first)
        ns.add(n)
        all_nodes.add(n)

print(len(all_nodes))

# viz
# dot -Tsvg -Kneato input.file -o out.svg
"""
with open('viz.txt', 'w') as f:
    f.write('graph {\n')
    for node, connected in nodes.items():
        for oc in connected:
            f.write(f'{node} -- {oc}\n')
    f.write('}')
"""

breaks = (
    ('bdj' , 'vfh'),
    ('bnv' , 'rpd'),
    ('ztc' , 'ttv'),
)

for j, k in breaks:
    nodes[j].remove(k)
    nodes[k].remove(j)


def connected(start: str) -> int:
    visited = set()
    current = deque()
    current.append(start)

    while current:
        n = current.pop()
        if n in visited:
            continue
        visited.add(n)

        for other in nodes[n]:
            if other in visited:
                continue
            current.append(other)

    return len(visited)

x, y = connected('bdj'), connected('vfh')
print(x, y, x*y)


