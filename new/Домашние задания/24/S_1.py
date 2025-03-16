import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.1.txt') as f:
    s = f.readline()

    m = 10**10
    l = c = 0

    for r in range(1,len(s)):
        if s[r] == s[r-1] == 'T':
            c+=1
        while c>=150:
            l+=1
            if s[l]+s[l-1]=='TT': c-=1
        if c==149: m = min(r - l + 2, m)
                
    print(m)