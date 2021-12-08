with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

inputs = [_.partition(' | ')[0].split() for _ in lines]
outputs = [_.partition(' | ')[2].split() for _ in lines]

from collections import defaultdict

"""
1: 2

7: 3

8: 7
6: 6
9: 6
0: 6

4: 4
2: 5
3: 5
5: 5
"""

nums = []

for input, output in zip(inputs, outputs):
    final = defaultdict(set)
    lens = defaultdict(set)

    for number in input:
        size = len(number)
        lens[size] |= set(number)
    for number in output:
        size = len(number)
        lens[size] |= set(number)

    final[1] = lens[2]
    final[4] = lens[4]
    final[7] = lens[3]
    final[8] = lens[7]

    for number in input:
        size = len(number)
        number = set(number)
        if size == 6:
            if not final[6]:
                check6 = number | final[1] | final[7]
                if check6 == final[8]:
                    final[6] = number
                    continue
            if not final[0]:
                check0 = number | final[1]
                check01 = number | final[4]
                if check0 == number and check01 != number:
                    final[0] = number
                    continue
            if not final[9]:
                final[9] = number
                continue
        if size == 5:
            if not final[2]:
                check2 = number | final[4]
                if check2 == final[8]:
                    final[2] = number
                    continue
            if not final[3]:
                check3 = number | final[1]
                if check3 == number:
                    final[3] = number
                    continue
            if not final[5]:
                final[5] = number

    # print('\n'.join(f'{k} {v}' for k, v in sorted(final.items())))

    def set_lookup(set):
        for key, value in final.items():
            if value == set:
                return str(key)

    word = ''.join(set_lookup(set(_)) for _ in output)
    nums.append(int(word))

print(sum(nums))
