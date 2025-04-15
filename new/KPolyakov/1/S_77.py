import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from itertools import *

table = '235 1346 1257 26 137 24 35'.split()
graph = 'БВ АВ АБГД ВДЕК ВГК ГК ГДЕ'.split()

for p in permutations('АБВГДЕК'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1 in graph for c2 in graph):
        print(''.join(p))
        break