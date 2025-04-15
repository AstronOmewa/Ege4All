import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.11228.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]
    
    c = 0

    for l in ls:
        p = [l[i] for i in range(1, len(l)) if l[i]==l[i-1]]
        np =  [l[i] for i in range(1, len(l)) if l[i] not in p]
        l = sorted(l)

        if len([x for x in l if l.count(x)==3])==3 and\
        len([x for x in l if l.count(x)==2])==4 and\
        [x%2 for x in l[:4]].count(1)==2:
            c+=sum(l)
        
    print(c)    