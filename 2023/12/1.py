

with open('input.txt', 'r') as f:
    data = f.read().splitlines()



class Row:
    def __init__(self, data):
        springs, _, condition = data.partition(' ')

        self.springs: str = springs
        self.condition = tuple(int(i) for i in condition.split(','))

    def __str__(self):
        return f'<{self.springs} {self.condition}>'


class Builder:

    def __init__(self):
        self.last_char = ''
        self.seq = []
        self.current_section_len = 0
        self.section_lens = []

    def append(self, char: str):
        if char == '.' and self.last_char == '#':
            self.section_lens.append(self.current_section_len)
            self.current_section_len = 0

        if char == '#':
            self.current_section_len += 1


        self.seq.append(char)
        self.last_char = char

    def check(self, condition: tuple[int, ...]) -> bool:
        if len(self.section_lens) > len(condition):
            return False
        for i, j in zip(self.section_lens, condition):
            if i != j:
                return False
        return True

    def final_check(self, condition: tuple[int, ...]) -> bool:
        if len(self.section_lens) != len(condition):
            return False
        for i, j in zip(self.section_lens, condition):
            if i != j:
                return False
        return True

    def copy(self):
        b = Builder()
        b.last_char = self.last_char
        b.current_section_len = self.current_section_len
        b.seq = self.seq.copy()
        b.section_lens = self.section_lens.copy()

        return b

    def __str__(self):
        return ''.join(self.seq)

    def __repr__(self):
        return str(self)


def solve(r: Row):
    bs = [Builder()]

    for char in r.springs:
        if char == '?':
            added = [b.copy() for b in bs]
            for b in bs:
                b.append('#')
            for b in added:
                b.append('.')

            bs.extend(added)
        else:
            for b in bs:
                b.append(char)

        bs = [b for b in bs if b.check(r.condition)]

    for b in bs:
        b.append('.')
    bs = [b for b in bs if b.final_check(r.condition)]


    #print(bs)
    print(len(bs))
    return len(bs)




rows = [Row(line) for line in data]
solve(rows[-1])

x = sum(solve(row) for row in rows)
print(x)
#for r in rows:
#    solve(r)

