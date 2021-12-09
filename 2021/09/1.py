with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

lines = [[int(_) for _ in line]for line in lines]


def check(i, j, index):
    for row, col in ((i-1, j), (i+1, j), (i, j+1), (i, j-1)):
        if not 0 <= row < len(lines):
            continue
        if not 0 <= col < len(lines[0]):
            continue
        if lines[row][col] <= index:
            return False
    return True


lowest = []

for i, row in enumerate(lines):
    for j, num in enumerate(row):
        c = check(i, j, num)
        if c:
            lowest.append(num)

print(sum(lowest) + len(lowest))
