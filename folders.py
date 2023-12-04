import os

folder: str = "2023"

for i in range(1, 26):
    folder_path = f'{folder}/{i}'
    try:
        os.mkdir(folder_path)
    except Exception as e:
        print(f'Error with day {i}:\n{e}')

