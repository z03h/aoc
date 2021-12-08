with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]
line = [int(_) for _ in lines[0].split(',')]

min_value = min(line)
max_value = max(line)
print(min(sum(abs(_ - i) for i in line) for _ in range(min_value, max_value+1)))
