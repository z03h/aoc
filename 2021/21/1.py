p1 = 4
p2 = 8

p1 = 2
p2 = 10


s1 = 0
s2 = 0

counter = 0
dice = 1


def get_dice(num):
    nums = [num, num+1, num+2]
    nums = [num if num <= 100 else num % 100 for num in nums]
    return nums


while s1 < 1000 and s2 < 1000:
    nums = get_dice(dice)
    if counter % 2 == 0:
        p1 += sum(nums)
        score = p1 % 10
        if not score:
            score = 10
        s1 += score
    else:
        p2 += sum(nums)
        score = p2 % 10
        if not score:
            score = 10
        s2 += score
    dice = nums[-1] + 1

    counter += 1
print('dice', counter*3)
print('s1', s1, p1)
print('s2', s2, p2)

print(counter *3 * min(s1, s2))

