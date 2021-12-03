from collections import defaultdict


with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

oo = []
oo_list = lines

coo = []
coo_list = lines


for i in range(len(lines[0])):
    c = defaultdict(list)
    if len(oo_list) == 1:
        oo.extend(oo_list[0][i:])
        break
    for word in oo_list:
        c[word[i]].append(word)

    if len(c['0']) > len(c['1']):
        oo_list = c['0']

        oo.append('0')
    else:
        oo_list = c['1']
        oo.append('1')


for i in range(len(lines[0])):
    if len(coo_list) == 1:
        print(''.join(coo) == coo_list[0])
        break
    c = defaultdict(list)
    for word in coo_list:
        c[word[i]].append(word)

    if len(c['0']) <= len(c['1']):
        coo_list = c['0']
        coo.append('0')
    else:
        coo_list = c['1']
        coo.append('1')

coo = int(''.join(coo),2)
oo =int(''.join(oo), 2)
print(coo * oo)
