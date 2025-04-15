def f1(x, y, z, w):
    return (w <= y) == (z <= x)

def f2(x, y, z, w):
    return (w <= y) and ((not x) == z)

from itertools import *

for a1, a2, a3, a4, a5 in product([0,1], repeat=5):

    t1 = [
        (0, a1, 0, 0),
        (0, 0, 0, a2),
        (0, 1, 1, a3)
    ]

    tf = [
        (0, a1, 0, 0, 0, 1),
        (0, 0, 0, a2, 0, a4),
        (0, 1, 1, a3, a5, 0)
    ]

    if len(tf) != len(set(tf)): continue

    for p in permutations('xyzw'):
        if [f1(**dict(zip(p, r))) for r in t1] == [0,0,a5] and\
              [f2(**dict(zip(p, r))) for r in t1] == [1,a4,0]:
            print(''.join(p))