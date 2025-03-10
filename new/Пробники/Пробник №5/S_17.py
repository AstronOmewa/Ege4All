import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('17-257.txt') as f:
    a = [int(x) for x in f.readlines()]
    minnch = min([x for x in a if x%2 != 0])
    maxnch = max([x for x in a if x%2 != 0])
    c, minsum = 0, 10**9
    for i in range(1, len(a)):
        if (a[i] + a[i-1])%2==0 and a[i] + a[i-1] > minnch+maxnch:
            c+=1
            minsum =  min(minsum,a[i] + a[i-1])

    print(c, minsum)