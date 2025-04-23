import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import *

alf = '0123456789' + ascii_uppercase + ''.join([chr(x) for x in range(10000)])

def q_to_10(x, q):
    x1 = x[::-1]
    s = 0
    for i in range(len(x1)):
        s += alf.index(x1[i]) * q**i
    return s

def x_to_q(x,q):
    a = ''
    if x == 0: return [0]
    while x > 0:
        a += alf[x%q]
        x //= q
    return a[::-1]

for y in range(1,10):
    x = alf[y]
    a = q_to_10(f'3{x}15{x}',15) + q_to_10(f'123',int(f'3{x}51')) + q_to_10(f'{y**y}',10) + \
        q_to_10(f'1{x}3',int(f'1{y}3')) + q_to_10(f'1{x}2',y+1)
    if a%13==0:
        print(x_to_q(a,13))
        break