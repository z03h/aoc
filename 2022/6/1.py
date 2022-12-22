from collections import deque

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

queue: deque[str] = deque(maxlen=4)

num_chars = 4
chars = iter(data)

for _ in range(4):
    char = next(chars)
    queue.append(char)

if len(set(queue)) == 4:
    print(num_chars)
    exit()

while 1:
    to_remove = queue.popleft()

    char = next(chars)
    queue.append(char)
    num_chars += 1

    if len(set(queue)) == 4:
        print(num_chars)
        exit()
