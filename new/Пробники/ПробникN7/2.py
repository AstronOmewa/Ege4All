def f(x,y,z,w):
    return (not w) and (x and (not z) or (not x) and (not y) and z)

from itertools import *
t = [
        (0,0,0,1),
        (0,0,1,1),
        (1,0,0,0)
    ]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, r))) for r in t] == [1,1,1]:
        print(''.join(p))