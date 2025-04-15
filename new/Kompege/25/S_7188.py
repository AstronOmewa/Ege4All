from math import sqrt

def isprime(n):
    for x in range(2,int(sqrt(n)+1)):
        if n%x==0: return False

    return True

from fnmatch import fnmatch

for x in range(35155307,10**9,2423):
    if fnmatch(str(x),'3*51?5*7') and isprime(sum(int(y) for y in str(x))):
        print(x, x//2423)