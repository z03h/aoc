

with open('input.txt', 'r') as f:
    text = f.read()

max_dict = {
    'red': 0,
    'green': 0,
    'blue': 0,
}

def power(batches: str) -> int:
    max_dict = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for batch in batches.split('; '):
        for color_line in batch.split(', '):
            num, _, color = color_line.partition(' ')
            if int(num) > max_dict[color]:
                max_dict[color] = int(num)
    return max_dict['red'] * max_dict['green'] * max_dict['blue']


total = []
for line in text.split('\n'):
    game_text, _, batches = line.partition(': ')
    _, _, game_id = game_text.partition(' ')

    total.append(power(batches))

print(sum(total))





