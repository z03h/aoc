with open('test') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

lines = [eval(line) for line in lines]

import json
from dataclasses import dataclass


@dataclass
class Node:
    left: int = None
    right: int = None
    level: int = 0
    parent = None

    @classmethod
    def add(cls, left, right):
        if left.level != right.level:
            print('not equal levels')
        n = Node(left=left, right=right, level=left.level)
        left.deepen()
        right.deepen()
        left.parent = right.parent = n
        # check explode/split
        return n

    def deepen(self):
        self.level += 1
        if isinstance(self.left, type(self)):
            self.left.deepen()
        if isinstance(self.right, type(self)):
            self.right.deepen()

    @property
    def str(self):
        left = self.left if isinstance(self.left, int) else self.left.str
        right = self.right if isinstance(self.right, int) else self.right.str
        return f'[{left},{right}]'

    @property
    def root(self):
        p = self.parent
        if p is None:
            return self
        while p.parent is not None:
            p = p.parent
        return p

    def should_explode(self):
        return self.level >= 4

    def explode(self):
        x = False
        if not isinstance(self.left, int):
            x = x or self.left.explode()
        if not isinstance(self.right, int):
            x = x or self.right.explode()

        if self.level >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            print(self.str, 'explode', self.level)
            # explode
            # check if self is left or right
            is_left = self.parent.left is self
            if is_left:
                L, side = self.find_next_left()
                if L:
                    setattr(L, side, getattr(L, side) + self.left)

                R = self.parent.right
                if isinstance(R, int):
                    self.parent.right += self.right
                    R = self.parent
                else:
                    while isinstance(R.left, Node):
                        R = R.left
                    # found left most node right of self?
                    R.left += self.right

                self.parent.left = 0
            else:
                # is right side
                R, side = self.find_next_right()
                if R:
                    setattr(R, side, getattr(R, side) + self.right)
                L = self.parent.left

                if isinstance(L, int):
                    self.parent.left += self.left
                    L = self.parent
                else:
                    while isinstance(L.right, Node):
                        L = L.right
                    # found left most node right of self?
                    L.right += self.left
                self.parent.right = 0
            x = True
        return x

    @staticmethod
    def split(node):
        if isinstance(node.left, Node):
            node.split(node.left)
        elif node.left >= 10:
            L = node.left//2
            R = (L + 1) if node.left % 2 else L
            node.left = Node(left=L, right=R, level=node.level + 1)
            node.left.parent = node
        if isinstance(node.right, Node):
            node.split(node.right)
        elif node.right >= 10:
            L = node.right//2
            R = (L + 1) if node.right % 2 else L
            node.right = Node(left=L, right=R, level=node.level + 1)
            node.right.parent = node

    def find_next_left(self):
        p = self.parent
        pp = p.parent
        side = 'right'
        if p is pp.right and isinstance(pp.left, int):
            side = 'left'
            return pp, side

        while pp is not None:
            if p is pp.right:
                break
            p = pp
            pp = p.parent
        if pp is None:
            return None, None

        if isinstance(pp.left, Node):
            pp = pp.left
            # get left most node right
            if isinstance(pp.right, Node):
                while isinstance(pp.right, Node):
                    pp = pp.right
            return pp, side
        else:
            return pp, 'left'

    def find_next_right(self):
        p = self.parent
        pp = p.parent
        side = 'left'
        if p is pp.left and isinstance(pp.right, int):
            side = 'right'
            return pp, side

        while pp is not None:
            if p is pp.left:
                break
            p = pp
            pp = p.parent
        if pp is None:
            return None, None

        if isinstance(pp.right, Node):
            pp = pp.right
            # get left most node right
            if isinstance(pp.left, Node):
                while isinstance(pp.left, Node):
                    pp = pp.left
            return pp, side
        else:
            return pp, 'right'


def parse_list(input, level=0):
    left = input[0]
    right = input[1]
    if isinstance(left, list):
        left = parse_list(left, level+1)

    if isinstance(right, list):
        right = parse_list(right, level+1)

    n = Node(left=left, right=right, level=level)
    if isinstance(left, Node):
        left.parent = n
    if isinstance(right, Node):
        right.parent = n
    return n


lines = [parse_list(L) for L in lines]

for line in lines:
    x=True
    print(line.str)
    while x:
        x = line.explode()
        print('===', line.str)

    print(line.str, '\n')
