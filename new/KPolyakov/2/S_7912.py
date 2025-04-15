def f(x, y, z, w):
    return not (( not x or y) and not w) or not(z and not (y and w))

from itertools import *

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):

    t = [
        (0, a1, a2, 1),
        (a3, 1, a4, a5),
        (1, 0, a6, a7)
    ]

    if len(t) != len(set(t)): continue

    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in t] == [0,0,0]:
             print(''.join(p))

