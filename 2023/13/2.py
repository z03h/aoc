

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
            total_diff = 0
            for line in lines:
                left = line[i-len_list:i]
                right = line[i+i-1:i-1:-1]
                total_diff += self.diff_line(left, right)
                if total_diff > 1:
                    break

            #if all(line[i-len_list:i]== line[i+i-1:i-1:-1] for line in lines):
            #    return i

            if total_diff == 1:
                return i

        return None

    @staticmethod
    def diff_line(line1: list[str], line2: list[str]) -> int:
        diff = sum(c1 != c2 for c1, c2 in zip(line1, line2))


        return diff

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

