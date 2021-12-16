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
                    subpackets.append((stype, svalue))
                    if start - bit_check >= Lbit:
                        # reached number of bits
                        break
            else:
                # number of packets
                for _ in range(Lbit):
                    # parse subpackets
                    index, sversion, stype, svalue = parse(start)
                    subpackets.append((stype, svalue))
                    start = index
            index = start
            return index, version, type, subpackets
    except ValueError:
        traceback.print_exc()
        return index, None, None, None


working_index = version= type= value = None
working_index = 0
versions = 0
b = False
count = 0

working_index, version, type, value = parse(working_index)


def unpack_value(type, value):
    if type == 4:
        return value

    if len(value) == 1:
        return unpack_value(*(value[0]))

    if type == 0:
        # sum
        parsed = [unpack_value(*v) if isinstance(v, tuple) else v for v in value]
        return sum(parsed)
    elif type == 1:
        # product
        parsed = [unpack_value(*v) if isinstance(v, tuple) else v for v in value]
        x = 1
        for i in parsed:
            x *= i
        return x
    elif type == 2:
        # minimum
        parsed = [unpack_value(*v) if isinstance(v, tuple) else v for v in value]
        return min(parsed)
    elif type == 3:
        # maximum
        parsed = [unpack_value(*v) if isinstance(v, tuple) else v for v in value]
        return max(parsed)
    elif type == 5:
        # greater than
        v1 = unpack_value(*value[0])
        v2 = unpack_value(*value[1])
        return int(v1 > v2)
    elif type == 6:
        # less than
        v1 = unpack_value(*value[0])
        v2 = unpack_value(*value[1])
        return int(v1 < v2)
    elif type == 7:
        # equal
        v1 = unpack_value(*value[0])
        v2 = unpack_value(*value[1])
        return int(v1 == v2)


print(unpack_value(type, value))
