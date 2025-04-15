from itertools import *


def f1(x, y, z, w):
    return (x <= y) or ((not w) == z)


def f2(x, y, z, w):
    return (x <= y) == ((w) and (not z))


for a1, a2, a3, a4, a5, a6, a7, a8, a9 in product([0, 1], repeat=9):

    t = [
        (a1, a2, a3, 0),
        (a4, a5, 0, 0),
        (a6, 0, 0, 0)
    ]
    t1 = [
        (a1, a2, a3, 0, a7, a7),
        (a4, a5, 0, 0, a8, a8),
        (a6, 0, 0, 0, a9, a9)
    ]
    if len(t1) != len(set(t1)): continue

    for p in permutations('xyzw'):
        if [f1(**dict(zip(p, r))) for r in t] == [a7, a8, a9] and [f2(**dict(zip(p, r))) for r in t] == [a7, a8, a9]:
            print(''.join(p))
