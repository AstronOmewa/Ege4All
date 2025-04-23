import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import hexdigits, ascii_uppercase
from itertools import product

alf = '0123456789' + ascii_uppercase + ''.join([chr(x) for x in range(128, 10000)])

def fr(x, q):
    a = 0
    x1 = x[::-1]
    for i in range(len(x1)):
        a += alf.index(x1[i]) * q ** i
    return a

for p in range(2,100):
    for q in range(p):
        if fr('ABC', p) == fr('BCD', q):
            print(fr('BCD', q),q, p)

print(fr('BCD',20), fr('ABC',21))