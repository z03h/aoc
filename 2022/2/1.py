
ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'
play_lookup = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

WIN = 6
DRAW = 3
LOSS = 0

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

pairs = data.split('\n')

score = 0

for line in pairs:
    opponent, player = line.split()
    player_val = play_lookup[player]
    opponent_val = play_lookup[opponent]

    score += player_val

    if opponent_val == player_val:
        score += DRAW
    else:
        if player_val == (opponent_val%3)+1:
            score += WIN

print(score)
