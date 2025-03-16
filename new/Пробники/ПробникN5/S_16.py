from functools import lru_cache
from sys import setrecursionlimit

f = [0,0,1,2]

for x in range(4,5000):
    if x%2 == 0:
        f.append(f[x-2] + x/2 - f[x-4])
    else:
        f.append(f[x-1]*x + f[x-2])
    

print(f[4952] + 2*f[4958]+f[4964])
print(f[3])