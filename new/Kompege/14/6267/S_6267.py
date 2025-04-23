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

for x in alf[:36][::-1]:
    if (fr(f'12{x}45', 36) + fr(f'1{x}', 12345)) % 13 == 0:
        print((fr(f'12{x}45', 36) + fr(f'1{x}', 12345))//13)
        break