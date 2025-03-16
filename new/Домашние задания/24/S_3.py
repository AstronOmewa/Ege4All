import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.3.txt') as f:
    s = f.readline()

    dp = [1]*len(s)

    for r in range(len(s)-1):
        if int(s[r])<int(s[r-1]): dp[r]=dp[r-1]+1
    
    print(max(dp))