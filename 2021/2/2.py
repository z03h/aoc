with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

h = 0
d = 0
aim = 0

for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    if direction == 'forward':
        h += amount
        d += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
print(h*d)
