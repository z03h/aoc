with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

from collections import Counter

gamma = []
epsilon = []

for i in range(len(lines[0])):
    c = Counter(word[i] for word in lines)
    if c['0'] > c['1']:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')
print(gamma, epsilon)
print(int(''.join(gamma),2) * int(''.join(epsilon), 2))
