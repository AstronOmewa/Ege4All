import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.9778.txt') as f:
    ls = [tuple(map(int, x.split())) for x in f.readlines()]

    for i in range(len(ls)):
        l = sorted(ls[i])
        k2 = [x for x in l if l.count(x)==2]

        if len(k2)==2\
              and k2[0]>=(sum(l)-sum(k2))/4:
            print(i+1)
            break
