
_LOSS = 'X'
_DRAW = 'Y'
_WIN = 'Z'


play_lookup = {
    'A': 1,
    'B': 2,
    'C': 3,
}

outcome_lookup = {
    _WIN: 6,
    _DRAW: 3,
    _LOSS: 0,
}

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

pairs = data.split('\n')

score = 0

for line in pairs:
    opponent, outcome = line.split()
    outcome_val = outcome_lookup[outcome]
    opponent_val = play_lookup[opponent]

    score += outcome_val

    if outcome == _DRAW:
        score += opponent_val
    elif outcome == _WIN:
        score += opponent_val % 3 + 1
    elif outcome == _LOSS:
        score += (opponent_val + 1) % 3 + 1

print(score)
