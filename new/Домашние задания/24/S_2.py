import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.2.txt') as f:
    s = f.readline()

    for x in 'ACDFO':
        if x in 'AO':
            y = 'A'
        else:
            y = 'B'
        s = s.replace(x,y) 

    s = s.replace('BA','x')

    print(s[:100])

    dp = [0]*len(s)

    for r in range(1,len(s)-1):
        if s[r] == 'x': dp[r] = dp[r-1]+1
    
    print(max(dp))