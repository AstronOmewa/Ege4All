import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

c = 0

with open('Q_9.txt') as f:
    for line in f.readlines():
        a = [int(x) for x in line.split()]
        mx, mn = max(a), min(a)

        if (len(a)==len(set(a))) and ((sum(a)-mx-mn)/len(a) < (mx+mn)/2):
            c+=1

    print(c)