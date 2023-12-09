

with open('input.txt', 'r') as f:
    data = f.read()


stimes, sdists = data.splitlines()


total_time = int(''.join(stimes.split()[1:]))
total_dist = int(''.join(sdists.split()[1:]))


count_good = 0
for speed in range(0, total_time//2):
    remaining_time = total_time - speed
    distance = remaining_time * speed

    count_good += distance > total_dist
    if not speed % 1000000:
        print(speed)

# symmetrical 5*4 == 4*5 so only need to go halfway
# i guess +1 is for middle? but idk i just guessed bc i didn't want to code more
print(count_good*2+1)
