import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import hexdigits
hexdigits = hexdigits.upper()
def to_q(x10, q):
    a = ''
    while x10>0:
        a += hexdigits[x10%q]
        x10 //= q
    return a[::-1]

for x in hexdigits[::-1]:
    a = int(f'B7A{x}9', 16) + int(f'54{x}ED', 16)
    if sum([int(x) for x in to_q(a,6)]) == 25:
        print(a)