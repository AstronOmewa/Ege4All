import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6783.txt') as f:
    s = f.readline()

    m = [1]*len(s)

    for i in range(len(s)):
        if s[i]!= s[i-1]:
            m[i] = m[i-1] + 1
    
    print(max(m))