def f(x,y,z,w):
    return not((((((w and x) == x) or 1) <= z) or ( not x)) and y)

from itertools import *

for a1, a2, a3, a4 in product([0,1], repeat=4):
    t = [
        (a1,a2,1,0),
        (1,a3,1,0),
        (a4,0,0,1)
    ]

    if len(t)!=len(set(t)): continue

    for p in permutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
            print(''.join(p))