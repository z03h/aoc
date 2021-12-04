with open('input') as f:
    lines = f.read().split('\n\n')
lines = [_ for _ in lines if _]

numbers, *tboards = lines


class Board:
    def __init__(self, text):
        self.numbers = {}
        self.rnumbers = {}
        for i, line in enumerate(text.split('\n')):
            for j, num in enumerate(line.split()):
                self.rnumbers[(i, j)] = False
                self.numbers[num] = (i, j)
        self.rows = max(n[0] for n in self.rnumbers)
        self.cols = max(n[1] for n in self.rnumbers)

    def mark(self, number):
        try:
            ij = self.numbers[number]
        except KeyError:
            return False
        self.rnumbers[ij] = True
        return self.check_bingo(*ij)

    def check_bingo(self, i, j):
        cols = all(self.rnumbers[(i, _)] for _ in range(self.cols+1))
        rows = all(self.rnumbers[(_, j)] for _ in range(self.rows+1))
        """if i == j or (i+j)==self.rows:
            diag = (
                all(self.rnumbers[(_, _)] for _ in range(self.cols)) or
                all(self.rnumbers[(_, self.cols-_-1)] for _ in range(self.cols))
            )
        else:
            diag = False
        """
        return rows or cols #or diag

    def check(self):
        sums = sum(int(n) for n, ij in self.numbers.items() if not self.rnumbers[ij])
        return sums


boards = [Board(b.strip()) for b in tboards]

for number in numbers.split(','):
    print(number)
    for board in boards:
        if board.mark(number):
            c = board.check()
            print(c * int(number), number, c)
            exit()
