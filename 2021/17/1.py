with open('test') as f:
    lines = f.read().strip()
xr, yr = lines[13:].split(', ')

xlow, xhigh = xr.strip('x=').partition('..')
ylow, yhigh = yr.strip('y=').partition('..')

xlow = int(xlow)
xhigh= int(xhigh)
ylow = int(ylow)
yhigh = int(yhigh)

print(121 * 122 /2)
# ok then
# I didn't need any of this
# it's just abs(lowest y pos) - 1

# since going up is just sum(1..y), going down is sum(1..y)
# it ends up back at 0
# so the next step goes -y - 1
