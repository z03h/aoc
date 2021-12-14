with open('input') as f:
    template, insert = f.read().split('\n\n')
    insert = insert.split('\n')

from collections import Counter

insert = [_.split(' -> ') for _ in insert if _]
insert = {k: v for k, v in insert}

mapping = Counter()

first = template[:2]

for i in range(2, len(template)+1):
    start = template[i-2:i]
    mapping[start] += 1


for _ in range(40):
    copy = Counter()
    ifirst = insert.get(first)
    if ifirst:
        first = first[0] + ifirst

    for word, count in mapping.items():
        if not count:
            continue
        insertion = insert.get(word)
        if insertion:
            copy[f'{word[0]}{insertion}'] += count
            copy[f'{insertion}{word[1]}'] += count
            copy[word] -= count
    for word, count in copy.items():
        mapping[word] += count

total = Counter()
for word, count in mapping.items():
    if count:
        # total[word[0]] += count
        total[word[1]] += count

total[first[0]] += 1
tv = total.values()
print(max(tv) - min (tv))
