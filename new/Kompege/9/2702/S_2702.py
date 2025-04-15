import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.2702.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]
    sum = 0

    for l in ls:
        l = sorted(l)[::-1]
        print(set(l))
        if len(set(l)) <= 2:
            if l.count(l[0])==2: sum+=(l[-1])
            else: sum+=l[0]
        
    print(sum)