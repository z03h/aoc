import functools

with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

lines = [_.split() for _ in lines]


@functools.cache
def split(input):
    x, y, z = input.split(',')
    x = [int(_) for _ in x[2:].split('..')]
    y = [int(_) for _ in y[2:].split('..')]
    z = [int(_) for _ in z[2:].split('..')]
    return x, y, z


def check_overlap(ox1,ox2,oy1,oy2,oz1,oz2,x1,x2,y1,y2,z1,z2):
    if x1>ox2 or x2<ox1: return False
    if y1>oy2 or y2<oy1: return False
    if z1>oz2 or z2<oz1: return False
    return True

def get_overlap(box1, box2):
    x1,y1,z1 = box1
    x2,y2,z2 = box2
    if check_overlap(*x1,*y1,*z1, *x2,*y2,*z2):
        # get overlapped section
        xl = x1[0], x2[0]
        xr = x1[1], x2[1]

        yl = y1[0], y2[0]
        yr = y1[1], y2[1]

        zl = z1[0], z2[0]
        zr = z1[1], z2[1]

        x = max(xl), min(xr)
        y = max(yl), min(yr)
        z = max(zl), min(zr)
        return x, y, z
    return None


# list of lists
# L[0] status
# L[1] og box
# L[2] to add or remove
# L[3] = overlaps with previous

output = []
for i, (status, box) in enumerate(lines):
    box = split(box)
    x,y,z = box

    if status == 'on':
        for line, s in output[:]:
            xx,yy,zz = line
            overlap = get_overlap(box, line)
            if overlap:
                output.append((overlap, -s))
        output.append((box, 1))
    elif status == 'off':
        for line, s in output[:]:
            xx,yy,zz = line
            overlap = get_overlap(box, line)
            if overlap:
                output.append((overlap, -s))

def count():
    t = 0
    for box, s in output:
        x, y, z = box
        x = x[1] - x[0] + 1
        y = y[1] - y[0] + 1
        z = z[1] - z[0] + 1
        t += x * y * z * s
    print(t)
count()
