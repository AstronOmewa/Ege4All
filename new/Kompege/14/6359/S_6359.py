import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import ascii_uppercase

alf = '0123456789' + ascii_uppercase + ''.join([chr(x) for x in range(129,10000)])

def to_q(x10, q):
    a = ''
    while x10 > 0:
        a += alf[x10 % q]
        x10 //= q
    return a[::-1]

def fr(x, q):
    a = 0
    x1 = x[::-1]
    for i in range(len(x1)):
        a += alf.index(x1[i]) * q ** i
    return a

for p in range(200):
    for x in alf[:p]:
        for y in alf[:p]:
            if fr(f'{x}{x}{x}8', p) + fr(f'43{x}9', p) == fr(f'{y}{y}04', p):
                print(fr(f'{y}{y}{x}', p))
                exit()

