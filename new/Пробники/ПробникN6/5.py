from itertools import *

for n in range(10**6):
    x = bin(n)[2:]
    if '0' in x:
        x = x[:x.rfind('0')]+x[:2]+x[x.rfind('0')+1:]
    else: continue

    x = x[::-1]

    r = int(x,2)

    if r == 123:
        print(n)
        break