
filename = 'input.txt'

with open(filename) as f:
    data = f.read()


trees = []
for line in data.split('\n'):
    trees.append(
        [int(x) for x in line]
    )

visible = set()
ROWS = len(trees)
COLS = len(trees[0])

# add outside edge
for i in range(COLS):
    visible.add((0, i))
    visible.add((ROWS-1, i))

for i in range(ROWS):
    visible.add((i, 0))
    visible.add((i, COLS-1))

for i in range(1, COLS-1):
    # go down each column
    tallest_tree = trees[0][i]
    for j in range(1, ROWS-1):
        current_tree = trees[j][i]
        if current_tree > tallest_tree:
            visible.add((j, i))
            tallest_tree = current_tree

    # go up each column
    tallest_tree = trees[ROWS-1][i]
    for j in range(ROWS-2, 0, -1):
        current_tree = trees[j][i]
        if current_tree > tallest_tree:
            visible.add((j, i))
            tallest_tree = current_tree

for j in range(1, ROWS-1):
    # go right each row
    tallest_tree = trees[j][0]
    for i in range(1, COLS-1):
        current_tree = trees[j][i]
        if current_tree > tallest_tree:
            visible.add((j, i))
            tallest_tree = current_tree

    # go left each row
    tallest_tree = trees[j][COLS-1]
    for i in range(COLS-2, 0, -1):
        current_tree = trees[j][i]
        if current_tree > tallest_tree:
            visible.add((j, i))
            tallest_tree = current_tree


print(len(visible))
