import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from itertools import product

for q,w,e in product('0123',repeat=3):
    for r,t in product('01234567',repeat=2):
        for y in '0123456789ABCDEF':
            if int(f'13{q}{w}22{e}', 4) == int(f'1{r}{t}50', 8) == int(f'{y}C28', 16):
                print(int(f'13{q}{w}22{e}', 4))
