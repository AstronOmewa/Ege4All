from itertools import *

with open("D:\\egeAll\\24\\py\\1_24.txt") as f:
    s = f.readline()

    l, mx, k = 0, 0, 1

    num, sym = [''.join(x) for x in product('124', repeat=2)], [''.join(y) for y in product('QRW', repeat = 2)]

    for r in range(1,len(s)):
        if all([s[r]+s[r-1] not in f for f in [num, sym]]):
            k+=1
        else:
            mx = max(mx, k)
            k = 1

    print(mx)