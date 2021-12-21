from itertools import product
from collections import Counter, defaultdict
from functools import cache

s1 = defaultdict(Counter)
s2 = defaultdict(Counter)


p1_start = 2
p2_start = 10

p1_start = 4
p2_start = 8


s1[0][p1_start] = 1
s2[0][p2_start] = 1

@cache
def get_dice(num):
    nums = [num, num+1, num+2]
    nums = [num if num <= 100 else num % 100 for num in nums]
    return Counter(sum(_)%10 for _ in product(nums, repeat=3))


rolls = get_dice(1)

player = 1

@cache
def get_score(turn, p1, p2, s1, s2):
    global player
    if s1 >= 21:
        return player
    if s2 >= 21:
        return not player
    t = 0

    for roll, rnum in rolls.items():
        p = p1 if turn else p2
        p = (roll + p) % 10
        p = p or 10
        if turn:
            # p1
            t += rnum * get_score(not turn, p, p2, s1+p, s2)
        else:
            # p2
            t += rnum * get_score(not turn, p1, p, s1, s2+p)
    return t


x = get_score(1, 2, 10, 0, 0)
player = 0
y = get_score(1, 2, 10, 0, 0)
print(x, y, max(x, y))
