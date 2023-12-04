from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


total_cards = defaultdict(lambda: 1)
for line in data:
    card, _, rest = line.partition(': ')
    card_num = int(card.split()[-1])
    total_current = total_cards[card_num]

    swinning, _, snumbers  = rest.partition(' | ')
    winning = set(int(i) for i in swinning.split())
    numbers = set(int(i) for i in snumbers.split())
    matched = len(winning & numbers) - 1
    if matched >= 0:
        for i in range(card_num+1, card_num+2+matched):
            total_cards[i] += total_current

print(sum(total_cards.values()))