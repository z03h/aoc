
from collections import defaultdict, deque
from PIL import Image, ImageDraw
import numpy as np

with open('test.txt', 'r') as f:
    data = f.read().splitlines()

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


DIRECTIONS = {
    'L': LEFT,
    'U': UP,
    'R': RIGHT,
    'D': DOWN,
}

row, col = 5, 5

points = []

for line in data:
    direction, num, color = line.split()
    num = int(num)
    dr, dc = DIRECTIONS[direction]
    dr *= num
    dc *= num
    points.append((row, col, row+dr, col+dc))
    row += dr
    col += dc




with Image.new('RGB', (20, 20), (255,255,255)) as im:
    d = ImageDraw.Draw(im)

    d.line(points[0], (0,0,0))

    for point in points[1:]:
        d.line(point, (0,0,0))
    im = im.rotate(-90).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im.save('test.png')


exit()
with Image.open('test.png') as im:
    im = im.convert('1')
    arr = np.array(im)
    count = np.count_nonzero(arr == 0)
print(count)