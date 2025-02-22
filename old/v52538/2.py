def f(a=0, b=0, c=0):
    return ((not a ) or (b) or (not c)) and (b or (not c))

from itertools import *

t = [
    tuple(int(i) for i in f'{x:03b}') for x in range(8)
]

print(t)
for p in permutations('abc'):
    if [f(**dict(zip(p,r))) for r in t] == [1,0,1,0,1,1,1,1]:
        print(''.join(p))