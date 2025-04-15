import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.9062.txt') as f:
    ls = [tuple(map(int, x.split())) for x in f.readlines()]

    c = 0

    for l in ls:
        if l[0] not in (max(l), min(l)) and\
        l[-1] not in (max(l), min(l)):  
            lp = sorted(l)
            print(lp)
            if  lp[2]!=lp[1] and (lp[-1]-lp[0])%(lp[2]-lp[1])==0:
                c+=1
    
    print(c)