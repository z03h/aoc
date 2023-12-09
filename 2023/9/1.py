import itertools

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    nums = [int(x) for x in line.split()]
    sands = [nums]
    while True:
        diff = [b - a for a, b in itertools.pairwise(nums)]
        if len(set(diff)) == 1:
            break
        sands.append(diff)
        nums = diff

    last_sum = diff[0]

    for sand in reversed(sands):
        new_end = sand[-1] + last_sum
        last_sum = new_end
    total += last_sum

print(total)




