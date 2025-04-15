import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.12918.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]

    c = 0

    for l in ls:
        k2 = [x for x in l if l.count(x)==2]
        p = [x for x in l if l.count(x)==1]
        if max(l)*min(l)>sum(l)-max(l)-min(l)\
              and (max(l) in p) and len(k2)==4:
            c=sum(l)
            break
    print(c)