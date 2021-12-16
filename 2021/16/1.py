with open('input') as f:
    line = f.read().strip()
line = ''.join(bin(int(c, 16))[2:].zfill(4) for c in line)

import traceback

def btoi(word):
    return int(word, 2)


def parse(index):
    try:
        version = btoi(line[index: index + 3])
        type = btoi(line[index + 3: index + 6])

        if type == 4:
            # literal
            start = index + 6
            bins = []
            while line[start] == '1':
                word = line[start + 1: start + 5]
                bins.append(word)
                start += 5
            word = line[start + 1: start + 5]
            bins.append(word)
            literal = btoi(''.join(bins))
            return start + 5, version, type, literal
        else:
            # operator
            subpackets = []
            start = index + 6
            id = line[start]
            length = 15 if id == '0' else 11
            start += 1
            Lbit = btoi(line[start: start + length])

            start = start + length
            if id == '0':
                # number of bits
                bit_check = start
                while True:
                    start, sversion, stype, svalue = parse(start)
                    subpackets.append((sversion, stype, svalue))
                    if start - bit_check >= Lbit:
                        # reached number of bits
                        break
            else:
                # number of packets
                for _ in range(Lbit):
                    # parse subpackets
                    index, sversion, stype, svalue = parse(start)
                    subpackets.append((sversion, stype, svalue))
                    start = index
            index = start
            return index, version, type, subpackets
    except ValueError:
        traceback.print_exc()
        return index, None, None, None


def unpack_versions(list):
    num = 0
    for version, type, value in list:
        if type == 4:
            num += version
        else:
            num += unpack_versions(value) + version
    return num



working_index = version= type= value = None
working_index = 0
versions = 0
b = False
count = 0

working_index, version, type, value = parse(working_index)

if type != 4:
    versions += unpack_versions(value)
versions += version

print(versions)
