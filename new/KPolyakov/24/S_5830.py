import os
from string import ascii_uppercase
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5830.txt') as f:
    s = f.readline()

    for x in ascii_uppercase:
        s = s.replace(x*2, ' ')

    a = [x for x in s.split()]
    
    m = max(a, key = len)
    d = dict()

    for x in m:
        if x in d.keys():
            d[x]+=1
        else:
            d[x] = 1
    
    print(max(d.values()))