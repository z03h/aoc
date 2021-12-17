with open('input') as f:
    lines = f.read().strip()
xr, yr = lines[13:].split(', ')

xlow, _, xhigh = xr.strip('x=').partition('..')
ylow, _, yhigh = yr.strip('y=').partition('..')

xlow = int(xlow)
xhigh= int(xhigh)
ylow = int(ylow)
yhigh = int(yhigh)

# find valid sums?
valid_x = {}
test_x = 1
for test_x in range(1, xhigh + 1):
    temp_sum = 0
    steps = 0
    for i in range(test_x, 0, -1):
        temp_sum += i
        steps += 1
        if xlow <= temp_sum <= xhigh:
            valid_x[(test_x, steps)] = []
        if temp_sum > xhigh:
            break

for (test_x, steps), valid in valid_x.items():
    for test_y in range(ylow, -ylow):
        sum_y = 0
        t_y = test_y
        for _ in range(steps):
            sum_y += t_y
            t_y -= 1
        if ylow <= sum_y <= yhigh:
            valid.append(test_y)
            continue
        if steps == test_x:
            # has run out of x velocity and is falling straight
            # continue going until it passes window
            while True:
                sum_y += t_y
                t_y -= 1
                if ylow <= sum_y <= yhigh:
                    valid.append(test_y)
                if sum_y < ylow:
                    break

total = set()
for (x, step), ys in valid_x.items():
    for y in ys:
        total.add((x,y))
print(len(total))
