

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


data = [list(row) for row in data]

for rownum, row in enumerate(data):
    for colnum, char in enumerate(row):
        if char != 'O':
            continue
        moved_row_num = rownum - 1
        current_row = row
        while moved_row_num >= 0:
            above_row = data[moved_row_num]
            if above_row[colnum] == '.':
                above_row[colnum] = 'O'
                current_row[colnum] = '.'
                current_row = above_row
                moved_row_num -= 1
            else:
                break
s = 0
for i, row in enumerate(reversed(data), 1):
    s += row.count('O') * i

print(s)
