import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from itertools import *
with open('9.6081.txt') as f:
    ls = [tuple(map(int, x.split())) for x in f.readlines()]

    c = 0

    for l in ls:
        kg2 = [x for x in l if l.count(x)>1]
        k2 = [x for x in l if l.count(x)==2]

        if len(kg2)==2 and len(k2)==2 and\
        any(l[i[0]]+l[i[1]]+l[i[2]] == l[i[3]]+l[i[4]]+l[i[5]] for i in permutations([0,1,2,3,4,5])):
            c+=1

    print(c)