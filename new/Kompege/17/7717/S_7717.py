import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('17.7717.txt') as f:
    s = [int(x) for x in f.readlines()]

    c, maxs = 0, 0
    maxel = max(s)
    for i in range(len(s)-1):
        a, b = s[i], s[i+1]
        if all(str(a)[i]>str(b)[j] for i in range(len(str(a))) for j in range(len(str(b))))\
            and a+b <= maxel:
            c += 1
            maxs = max(maxs, a+b)
        
    print(c, maxs)