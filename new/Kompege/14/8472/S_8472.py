import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import ascii_uppercase

alf = '0123456789' + ascii_uppercase + ''.join([chr(x) for x in range(129,10000)])

def fr(x,q):
    a = 0
    x1 = x[::-1]
    for i in range(len(x1)):
        a+=alf.index(x1[i])*q**i
    return a

def to_q(x10, q=6):
    a = ''
    while x10>0:
        a += alf[x10%q]
        x10 //= q
    return a[::-1]

ans = []
for x in alf[:100]:
    a = fr(f'7A{x}0123', 100) - fr(f'1BA64{x}',100) + fr(f'{x}98012C',100)
    if a%21 == 0:
        ans.append(alf.index(x))

print(to_q(max(ans)))
        