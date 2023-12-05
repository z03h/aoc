
# 12:39am start 12/05
#  1:22am done
with open('input.txt', 'r') as f:
    data = f.read()


class Node:
    def __init__(self, dest: int, source: int, size:int):
        self.dest = dest
        self.range = size
        self.source = source

    def get_matching(self, other: int) -> int | None:
        if self.source <= other < self.source + self.range:
            return self.dest + other - self.source
        return None

    def __str__(self):
        return f'[d={self.dest}, s={self.source}, r={self.range}]'

seeds = '79 14 55 13' # test
seeds = '3082872446 316680412 2769223903 74043323 4131958457 99539464 109726392 353536902 619902767 648714498 3762874676 148318192 1545670780 343889780 4259893555 6139816 3980757676 20172062 2199623551 196958359'


str_maps = data.split('\n\n')
maps: list[list[Node]] = []

for ms in str_maps:
    temp_m = []
    for m in ms.splitlines():
        if m[-1] == ':':
            continue
        temp_m.append(Node(*[int(i) for i in m.split()]))

    maps.append(temp_m)

current = [[int(i)] for i in seeds.split()]

for ms in maps:
    for i in current:
        matched_value = None
        for m in ms:
            matched_value = m.get_matching(i[-1])
            if matched_value is not None:
                break
        if matched_value is not None:
            i.append(matched_value)

lowest = (min(x[-1] for x in current))
print(lowest)




