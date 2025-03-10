from itertools import *

def f(x,y,z,w):
    return (w<=y) and ((x<=z) == (y<=x))

for a1, a2, a3, a4 in product([0,1], repeat=4):

    t = [
        (a1, 1, a2, 0),
        (0, a3, 1, a4),
        (0, 1, 0, 1  )
    ]

    if len(t)!=len(set(t)):
        continue

    for p in permutations('xyzw'):
        # print(''.join(p))
        if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
            print(''.join(p))