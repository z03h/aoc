with open('input') as f:
    template, insert = f.read().split('\n\n')
    insert = insert.split('\n')

from collections import Counter

insert = [_.split(' -> ') for _ in insert if _]
insert = {k: v for k, v in insert}

for _ in range(10):
    word = []
    for i in range(2, len(template)+1):
        start = template[i-2:i]
        to_insert = insert.get(start)
        word.append(start[0])
        if to_insert:
            word.append(to_insert)
    word.append(start[1])
    template = ''.join(word)
    print(len(template))

x = Counter(template)
top = max(x.values())
bot = min(x.values())
print(x)
print(top - bot)
