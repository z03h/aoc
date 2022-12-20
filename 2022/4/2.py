
filename = 'input.txt'

with open(filename) as f:
    data = f.read()

overlapped = 0

def in_range(num, lower, upper) -> bool:
    return lower <= num <= upper

for line in data.split('\n'):
    p1, p2 = line.split(',')
    elf1 = [int(x) for x in p1.split('-')]
    elf2 = [int(x) for x in p2.split('-')]
    if in_range(elf1[0], *elf2) or in_range(elf1[1], *elf2) or in_range(elf2[0], *elf1) or in_range(elf2[1], *elf1):
        overlapped += 1

print(overlapped)
