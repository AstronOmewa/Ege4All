def f(x, y, z, w):
    return ( not x and y and (not z) or x and (not y) ) and not w

from itertools import permutations, product

t = [
    (0,0,0,1),
    (1,0,0,0),
    (1,1,0,0)
]

for p in permutations('xyzw'):
    if [f(**dict(zip(p, r))) for r in t] == [1,1,1]:
        print(''.join(p))


# x z w y
# 0 0 0 1
# --> {x:0, z:0, w:0, y:1}