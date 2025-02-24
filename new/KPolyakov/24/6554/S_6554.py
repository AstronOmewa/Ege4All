import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6554.txt') as f:
    s = f.readline()

    p = [''.join(x) for x in product('02468','13579')] + [''.join(x) for x in product('13579','02468')]

    for x in p:
        s.replace(x, f'{x[0]} {x[1]}')

    print(s)

    print(max(len(x) for x in s.split()))