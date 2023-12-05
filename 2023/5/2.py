from __future__ import annotations



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

    def __repr__(self):
        return str(self)


class Translator:
    def __init__(self, nodes: list[Node]):
        nodes.sort(key=lambda n: n.source)
        self.nodes = nodes

    def translate(self, num: int , range: int):
        new_ranges = []
        low = num
        high = num + range


        for node in self.nodes:
            nlow = node.source
            nhigh = node.source + node.range

            if nlow > high:
                # range is completely below
                new_ranges.append((low, range))
                break

            if nlow <= high < nhigh:
                # some overlap, upper end of range overlaps node
                # find what overlap
                if low >= nlow:
                    # completely contained in node, only 1 range
                    diff = low - nlow
                    new_ranges.append((node.dest + diff, range))
                    break
                else:
                    # range overlaps node from lower end, 2 new ranges

                    # lower end that doesn't overlap
                    # dont translate
                    lower_range = nlow - low
                    new_ranges.append((low, lower_range))
                    # upper end overlaps the lower end of node, start from dest
                    upper_range = range - lower_range
                    new_ranges.append((node.dest, upper_range))

                    assert(lower_range+upper_range == range)

                    break

            if nlow <= low < nhigh:
                # some overlap, lower end of range overlaps node
                # high should be greater or eq to nhigh because it's already been checked
                diff = low - nlow
                lower_range = nhigh - low
                new_ranges.append((node.dest + diff, lower_range))

                # modify low and range for next nodes
                low = nhigh
                range -= lower_range


            if low < nlow and high >= nhigh:
                # range contains node

                # lower end that doesn't overlap
                # dont translate
                lower_range = nlow - low
                new_ranges.append((low, lower_range))

                # middle part completely overlaps
                new_ranges.append((node.dest, node.range))

                # upper part
                low = nhigh
                range -= lower_range + node.range

        if not new_ranges:
            new_ranges.append((low, range))

        return new_ranges


with open('input.txt', 'r') as f:
    data = f.read()

seeds = '79 14 55 13' # test
seeds = '3082872446 316680412 2769223903 74043323 4131958457 99539464 109726392 353536902 619902767 648714498 3762874676 148318192 1545670780 343889780 4259893555 6139816 3980757676 20172062 2199623551 196958359'


str_maps = data.split('\n\n')
maps: list[Translator] = []

for ms in str_maps:
    temp_m = []
    for m in ms.splitlines():
        if m[-1] == ':':
            continue
        temp_m.append(Node(*[int(i) for i in m.split()]))

    maps.append(Translator(temp_m))

init_seeds = seeds.split()
ranges = []
for i in range(0, len(init_seeds), 2):
    rr = [int(i) for i in init_seeds[i:i+2]]
    ranges.append(rr)


for map in maps:
    t_ranges = []

    for r in ranges:
        t_ranges.extend(map.translate(*r))

    ranges = t_ranges

print(min(x[0] for x in ranges))
