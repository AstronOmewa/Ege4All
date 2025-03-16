import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6784.txt') as f:
    s = f.readline()

    dp = [0]*len(s)

    for i in range(len(s)):
        if s[i-3:i+1] == 'CSGO':
            dp[i] = dp[i-4] + 4
        elif s[i-1:i+1] == 'PC':
            dp[i] = dp[i-2] + 2
         
    print(max(dp))