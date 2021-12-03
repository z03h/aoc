import os
import sys

BASE_URL = 'https://adventofcode.com/2021/day/{}/input'

day = sys.argv[1]
os.mkdir(day)

base_py = """with open('input') as f:
    lines = f.read().split('\\n')
lines = [_ for _ in lines if _]"""

with open(f'{day}/input', 'w') as f:
    ...
with open(f'{day}/test', 'w') as f:
    ...
with open(f'{day}/1.py', 'w') as f:
    f.write(base_py)
with open(f'{day}/2.py', 'w') as f:
    f.write(base_py)
