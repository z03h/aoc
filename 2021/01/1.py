with open('input') as f:
    l = f.read().split()

prev, *rest = l

num = 0
for n in rest:
    num += int(n) > int(prev)
    prev = int(n)
print(num)
