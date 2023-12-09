from collections import Counter


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

ordering = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
ordering.reverse()

ordering = {char: i for i, char in enumerate(ordering)}



class Hand:

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.rank = None

    def type(self):
        c = Counter(self.hand)
        vals = sorted(c.values(), reverse=True)[:2]

        t = tuple(ordering[c] for c in self.hand)
        self.rank = vals, t

        return tuple(vals), t

    def __repr__(self):
        return self.hand


hands = []
for hand_amount in data:
    hand, bid = hand_amount.split()
    hands.append(Hand(hand, bid))

hands.sort(key=lambda h: h.type())

total = 0
w = open('out.txt', 'w')
for i, hand in enumerate(hands, 1):
    total += i * hand.bid
    w.write(f'{hand} {hand.rank} {hand.bid} {i}\n')
w.close()
print(total)