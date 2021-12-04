with open('input') as f:
    l = f.read().split()

l = [int(n) for n in l]

prev = sum(l[:3])

num = 1
for i in range(2, len(l)-2):
    num += sum(l[i-1:i+2]) > prev
    prev = sum(l[i-1:i+2]) 
print(num)
