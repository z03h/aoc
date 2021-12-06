with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

line = lines[0]

from collections import Counter

# only need to keep track of how many fish are at each day
# not each fish
fishies = Counter()
fishies[8] = 0
fishies[-1] = 0

for i in line.split(','):
    fishies[int(i)] += 1

days = 256

for _ in range(days):
    for i in range(9):
        fishies[i - 1] = fishies[i]
        fishies[i] = 0
    new_fish = fishies[-1]
    fishies[-1] = 0
    fishies[8] += new_fish
    fishies[6] += new_fish

print(sum(fishies.values()))
