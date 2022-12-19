grid = '''2719 3271 1609 3881 2381 1087 1949 1889 2939 3169 3607 3823
3529 1409 1787 1553 2791 3919 2887 1823 1697 3947 1657 3727
3593 1811 2729 1801 2437 1153 2549 2591 1279 3373 1447 1871
1699 1459 1913 1783 3917 2789 3041 1283 3821 3709 1979 2411
2273 1607 3557 1523 1901 3191 2699 3659 2347 2539 1019 1723
2011 3251 3049 2459 1109 2819 2237 2399 2749 3499 1163 1303
3637 3449 1423 2803 1861 3307 1301 2473 3119 3889 2089 1867
3769 3467 1549 2129 1559 1531 1583 1907 1427 3461 2797 1031
2609 2879 1061 1973 3797 3079 1831 1051 2777 2081 3793 1249
2663 2671 3833 3371 2711 3533 1187 3203 1933 2909 2281 3697
2287 2003 1481 3347 2269 2063 1667 1747 1847 1367 1093 2203
1759 1069 2917 1721 1063 3259 1307 3037 2713 1471 1319 2801'''
x = [x.split() for x in grid.splitlines()]

with open('tt.txt', 'r') as f:
    x = f.read()

snap = x.split('\n\n')
tiles = {}
for s in snap:
    name, _, rest = s.partition('\n')
    _lmao, _lmoa, name = name.strip(':').partition(' ')
    name=int(name)
    #print(name, '\n', rest)
    tiles[name] = rest.splitlines()
