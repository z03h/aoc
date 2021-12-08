with open('input') as f:
    lines = f.read().split('\n')
lines = [_ for _ in lines if _]

outputs = [_.partition(' | ')[2].split() for _ in lines]


"""
1: 2

7: 3

8: 7
6: 6
9: 6
0: 6

4: 4
2: 5
3: 5
5: 5
"""

final = dict.fromkeys('abcdefg')

lookup = {
    1: {7: 'a'},
    8: {6: 'c', 9: 'e', 0: 'd'},
}
print(sum(sum(len(w) in (2, 3, 7, 4) for w in _) for _ in outputs))
