

with open('input.txt', 'r') as f:
    data = f.read()


class Pattern:
    def __init__(self, input: str):
        self._input = input
        self.colc = [list(x) for x in input.splitlines()]
        self.rowc = [[row[i] for row in self.colc] for i in range(len(self.colc[0]))]

    def __repr__(self):
        return self._input + '\n'


    def reverse_check(self, lines: list[list[str]]) -> int | None:
        len_line = len(lines[0])
        for i in range(1, len_line):
            len_list = min(len_line - i, i)
            # for line in lines:
            #     left = line[i-len_list:i]
            #     right = line[i+i-1:i-1:-1]
            #     print(i, left, '=', right)

            if all(line[i-len_list:i]== line[i+i-1:i-1:-1] for line in lines):
                return i

        return None


    def check(self) -> int:
        num_rows = self.reverse_check(self.rowc) or 0
        num_cols = 0
        if not num_rows:
            num_cols = self.reverse_check(self.colc) or 0

        return num_cols + num_rows * 100

spatterns = data.split('\n\n')

patterns = [Pattern(s) for s in spatterns]

x = sum(p.check() for p in patterns)
print(x)

