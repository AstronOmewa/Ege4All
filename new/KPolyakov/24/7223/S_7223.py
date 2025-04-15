import os
from string import ascii_uppercase
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.7223.txt') as f:
    l, m = 0, 0
    symcount = dict(zip(ascii_uppercase, [0]*len(ascii_uppercase)))
    # print(symcount)
    line = f.readline()
    for r in range(len(line)):
        
        symcount[line[r]]+=1

        while 2 in list(symcount.values()):
            
            symcount[line[l]]-=1
            l += 1
        
        m = max(r - l + 1, m)
    print(m)
        