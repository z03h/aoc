

with open('input.txt', 'r') as f:
    data = f.read().splitlines()



class Row:
    def __init__(self, data):
        springs, _, condition = data.partition(' ')

        self.springs: str = "?".join([springs]*5)
        self.condition = tuple(int(i) for i in condition.split(',')) * 5

    #def __init__(self, data):
    #    springs, _, condition = data.partition(' ')
#
    #    self.springs: str = springs
    #    self.condition = tuple(int(i) for i in condition.split(','))

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

class SingleBuilder:
    def __init__(self):
        self.last_char = '.'
        self.current_section_len = 0
        self.section_lens = tuple()
        self.count = 1

    def copy(self):
        b = SingleBuilder()
        b.last_char = self.last_char
        b.current_section_len = self.current_section_len
        b.section_lens = tuple(self.section_lens)
        b.count = self.count

        return b

    def append(self, char: str):
        if char == '.' and self.last_char == '#':
            self.section_lens += (self.current_section_len,)
            self.current_section_len = 0

        if char == '#':
            self.current_section_len += 1

        self.last_char = char

    def check(self, char, condition):
        new_section_lens = self.section_lens
        if char == '.' and self.last_char == '#':
            new_section_lens = self.section_lens + (self.current_section_len,)


        #new_len = self.current_section_len
        #if char == '#':
        #    new_len = self.current_section_len + 1

        if len(new_section_lens) > len(condition):
            return False
        for i, j in zip(new_section_lens, condition):
            if i != j:
                return False

        #try:
        #    if new_len > condition[len(new_section_lens)]:
        #        return False
        #except Exception:
        #    return False
        return True

    def finalcheck(self, char, condition):
        new_section_lens = self.section_lens
        if char == '.' and self.last_char == '#':
            new_section_lens = self.section_lens + (self.current_section_len,)

        if len(new_section_lens) != len(condition):
            return False
        for i, j in zip(new_section_lens, condition):
            if i != j:
                return False
        return True

    @property
    def key(self):
        return (self.last_char, self.current_section_len, self.section_lens)

    def __repr__(self):
        return f'<{self.last_char}|{self.section_lens}={self.count}>'


def solve2(r: Row):
    counter = {}
    b = SingleBuilder()
    counter[b.key] = b
    cond = r.condition

    for char in r.springs:
        new_counter = {}


        if char == '?':
            for _, b in counter.items():
                for tchar in ".#":
                    bb = b.copy()
                    if not bb.check(tchar, cond):
                        continue

                    bb.append(tchar)
                    key = bb.key
                    bbb = new_counter.get(key)
                    if bbb:
                        bbb.count += bb.count
                    else:
                        new_counter[key] = bb
        else:
            for _, b in counter.items():
                if not b.check(char, cond):
                    continue

                b.append(char)
                key = b.key
                bb = new_counter.get(key)
                if bb:
                    bb.count += b.count
                else:
                    new_counter[key] = b
        counter = new_counter

        #print(list(counter.values()))

    x = sum(b.count for b in counter.values() if b.finalcheck('.', cond))
    #print(x)
    return x


rows = [Row(line) for line in data]

import time
s = time.time()
x = sum(solve2(row) for row in rows)
print(x)
print(time.time()-s)

