with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

h = 0
d = 0
for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    if direction == 'forward':
        h += amount
    elif direction == 'down':
        d += amount
    elif direction == 'up':
        d -= amount

print(h*d)

