W = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
W = [2, 9, 9, 9, 1, 9, 9, 3, 6, 9, 8, 4, 6, 9]

#    0  1  2  3  4  5  6  7  8  9 10 11 12 13
W = [1, 4, 6, 9, 1, 2, 7, 1, 1, 1, 1, 1, 1, 1]
X = [15, 11, 10, 12, -11, 11, 14, -6, 10, -6, -6, -16, -4, -2]
Y = [9, 1, 11, 3, 10, 5, 0, 7, 9, 15, 4, 10, 4, 9]
Z = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]

while True:
    x = 0
    y = 0
    z = 0

    for i in range(14):
        z26 = z % 26
        goal = X[i] + z26
        if 1 <= goal <= 9:
            W[i] = goal

        z //= Z[i]
        x = W[i] != goal
        z *= (25 if x else 0) + 1
        z += (Y[i] + W[i]) * x
        print(f'{i=} {goal=} {X[i]=} {Y[i]=} {Z[i]=} {W[i]=} z={[z//26 ** _ for _ in range(14)]}')
        if X[i] < 10 and W[i] != goal:
            break

    print(W, ''.join(str(_) for _ in W), z)
    if z == 0:
        break
    exit()
