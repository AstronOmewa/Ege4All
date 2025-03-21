import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.4.txt') as f:
    s = f.readline()

    alf = [''.join(x) for x in product('QRS', repeat=2)]

    for x in alf:
        s = s.replace(x, x[0]+' '+x[1])
    
    print(s)
    s = s.split(' ')

    print(len(max(s, key=len)))