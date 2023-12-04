with open('input', 'r') as f:
    data = f.read()

valid = set('01234567890\n')
data = ''.join(c for c in data if c in valid)

lines = data.split()

x = sum(int(line[0] + line[-1]) for line in lines)
print(x)