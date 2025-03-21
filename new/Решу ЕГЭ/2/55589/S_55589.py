import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from itertools import *

f = open('Q_55589.txt')
f.close()

def f1(x,y,z,w):
    return (x<=y) == (w or (not z))

def f2(x,y,z,w):
    return (x<=y)and ((not w) == z)

for a1, a2, a3, a4, a5 in product([0,1], repeat=5):
    t = [
        (a1, 1, 0, 1),
        (a2, 0, 0, 0),
        (0, a3, 0, 0)
    ]

    if len(t) != len(set(t)): continue

    for p in permutations('xyzw'):
        if [f1(**dict(zip(p,r))) for r in t] == [a4, 0, 0] and [f2(**dict(zip(p,r))) for r in t] == [0, a5, 1]:
            print(''.join(p))