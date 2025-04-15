from itertools import *

alf = 'ТИКТОК'

s = set()

for p in permutations(alf):
    if all(p[i]!=p[i+1] for i in range(len(p)-1)):
        s.add(''.join(p))

print(s, len(s))
