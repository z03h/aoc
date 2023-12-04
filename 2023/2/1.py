

with open('input.txt', 'r') as f:
    text = f.read()

MAX_R = 12
MAX_G = 13
MAX_B = 14

max_dict = {
    'red': MAX_R,
    'green': MAX_G,
    'blue': MAX_B,
}

def check(batches: str) -> bool:
    for batch in batches.split('; '):
        for color_line in batch.split(', '):
            num, _, color = color_line.partition(' ')
            if int(num) > max_dict[color]:
                return False
    return True


total = []
for line in text.split('\n'):
    game_text, _, batches = line.partition(': ')
    _, _, game_id = game_text.partition(' ')

    if check(batches):
        total.append(int(game_id))

print(sum(total))





