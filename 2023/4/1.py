

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    card, _, rest = line.partition(': ')
    swinning, _, snumbers  = rest.partition(' | ')
    winning = set(int(i) for i in swinning.split())
    numbers = set(int(i) for i in snumbers.split())
    matched = len(winning & numbers) - 1
    if matched >= 0:
        total += 2 ** matched
        print(card, 2 ** matched)

print(total)