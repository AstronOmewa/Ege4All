import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6680.txt') as f:
    s = f.readline()

    dp = [0]*len(s)
    index = 0

    for i in range(6,len(s)):
        col = s[i-5:i+1]
        if dp[i-6] == '#' and all([x in '0987654321ABCDEF' for x in dp[i-5:i+1]]):
            if (int(col[:2], 16) > int(col[2:4], 16)) and (int(col[:2], 16) > int(col[4:], 16)):
                dp[i] += 1
        
    print(sum(dp))