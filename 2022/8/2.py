
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

highest_score = 0

for row, col in visible:
    current_score = 1
    current_tree = trees[row][col]
    # go up
    current_count = 0
    for j in range(row-1, -1, -1):
        current_count += 1
        if trees[j][col] >= current_tree:
            break
    current_score *= current_count

    # go down
    current_count = 0
    for j in range(row+1, ROWS):
        current_count += 1
        if trees[j][col] >= current_tree:
            break
    current_score *= current_count

    # go left
    current_count = 0
    for i in range(col-1, -1, -1):
        current_count += 1
        if trees[row][i] >= current_tree:
            break
    current_score *= current_count

    # go right
    current_count = 0
    for i in range(col+1, COLS):
        current_count += 1
        if trees[row][i] >= current_tree:
            break
    current_score *= current_count

    if current_score > highest_score:
        highest_score = current_score

print(highest_score)
