import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.8365.txt') as f:
    ls = [tuple(map(int, x.split())) for x in f.readlines()]
    c = 0

    for l in ls:
        l = sorted(l)
        if len(l)==len(set(l)) and\
        2*l[2] == l[-1]+l[0]   and\
        2*l[2] == l[1]+l[3]:
            c+=1
    
    print(c)