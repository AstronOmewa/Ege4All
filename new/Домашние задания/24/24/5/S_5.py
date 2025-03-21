import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5.txt') as f:
    s = f.readline()

    m = 0

    for x in 'abcdefghujklm'.upper():
        _ = s.replace(x,f'{x} {x}').split(' ')

        m = max(m,len(max(_,key=len)))

    print(m)