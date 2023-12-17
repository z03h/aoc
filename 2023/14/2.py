

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


data = [list(row) for row in data]

def north(data):
    for rownum, row in enumerate(data):
        for colnum, char in enumerate(row):
            if char != 'O':
                continue
            moved_row_num = rownum - 1
            while moved_row_num >= 0 and data[moved_row_num][colnum] == '.':
                moved_row_num -= 1
            moved_row_num += 1
            if moved_row_num != rownum:
                data[moved_row_num][colnum] = 'O'
                row[colnum] = '.'
    return data

def south(data):
    rdata = list(reversed(data))
    for rownum, row in enumerate(rdata):
        for colnum, char in enumerate(row):
            if char != 'O':
                continue
            moved_row_num = rownum - 1
            while moved_row_num >= 0 and rdata[moved_row_num][colnum] == '.':
                moved_row_num -= 1
            moved_row_num += 1
            if moved_row_num != rownum:
                rdata[moved_row_num][colnum] = 'O'
                row[colnum] = '.'

    return data

def west(data):
    for row in ((data)):
        for colnum, char in enumerate(row):
            if char != 'O':
                continue
            moved_col_num = colnum - 1
            while moved_col_num >= 0 and row[moved_col_num] == '.':
                moved_col_num -= 1
            moved_col_num += 1
            if moved_col_num != colnum:
                row[colnum] = '.'
                row[moved_col_num] = 'O'
    return data

def east(data):
    for  row in ((data)):
        for colnum, char in enumerate(reversed(row), 1):
            colnum = -colnum
            if char != 'O':
                continue
            moved_col_num = colnum + 1
            while moved_col_num < 0 and row[moved_col_num] == '.':
                moved_col_num += 1

            moved_col_num -= 1
            if moved_col_num != colnum:
                row[colnum] = '.'
                row[moved_col_num] = 'O'
    return data


def cycle_db(data):
    north(data)
    for row in data:
        print(''.join(row))
    print()
    west(data)
    for row in data:
        print(''.join(row))
    print()
    south(data)
    for row in data:
        print(''.join(row))
    print()
    east(data)
    for row in data:
        print(''.join(row))
    print()
    return data

def cycle(data):
    north(data)
    west(data)
    south(data)
    east(data)
    return data

def g_to_s(data):
    return '\n'.join(''.join(r) for r in data)


def pprint(data):
    for row in data:
        print(''.join(row))
    print()

seen = []
new = None
_ = 0
for _ in range(10000):
    cycle(data)
    new = g_to_s(data)
    if new in seen:
        break

    seen.append(new)

    if not _+1 % 1000:
        print(_)


# 3 4 5 6 7 8 9
#  1 2 3 4 5 6
loop = seen.index(new)
cycles = _
loop_len = cycles - loop
print('start', loop, 'loop', cycles, loop_len )


bil = 1_000_000_000
cycled = seen[loop:]

index = (bil-1-cycles) % loop_len

"""
for index, ss in enumerate(cycled):
    data = [list(row) for row in ss.split('\n')]
    s = 0
    for i, row in enumerate(reversed(data), 1):
        s += row.count('O') * i
    print('weight',s)
"""

data = [list(row) for row in cycled[index].split('\n')]
s = 0
for i, row in enumerate(reversed(data), 1):
    s += row.count('O') * i
print('weight',s)