
filename = 'input.txt'

with open(filename) as f:
    data = f.read()

overlapped = 0

for line in data.split('\n'):
    p1, p2 = line.split(',')
    elf1 = [int(x) for x in p1.split('-')]
    elf2 = [int(x) for x in p2.split('-')]
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
        overlapped += 1

print(overlapped)
