

with open('input.txt', 'r') as f:
    data = f.read()

sum = 0
for h in data.split(','):
    isum = 0
    for char in h:
        isum += ord(char)
        isum *= 17
        isum %= 256

    sum += isum

print(sum)