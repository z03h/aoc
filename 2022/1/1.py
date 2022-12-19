
filename = 'input.txt'

with open(filename) as f:
    data = f.read()

elves = []

for elf in data.split('\n\n'):
    elves.append([int(calorie) for calorie in elf.split('\n')])

print(max(sum(elf) for elf in elves))