

with open('input.txt', 'r') as f:
    data = f.read()


stimes, sdists = data.splitlines()

td = {int(t) : int(d) for t, d in zip(stimes.split()[1:], sdists.split()[1:])}


valid = []

for total_time, record_distance in td.items():
    count_good = 0
    for speed in range(0, total_time+1):
        remaining_time = total_time - speed
        distance = remaining_time * speed

        count_good += distance > record_distance

    valid.append(count_good)

i = 1

for x in valid:
    i *= x

print(i)

print(valid)
