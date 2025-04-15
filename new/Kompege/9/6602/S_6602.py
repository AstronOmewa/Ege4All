import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.6602.txt') as f:
    ls = [list(map(int, l.split())) for l in f.readlines()]

    c = 0
    for k in ls:
        l = sorted(k)
        p = [l[i] for i in range(1,len(l)) if l[i-1]==l[i]]
        np = [l[i] for i in range(len(l)) if l[i] not in p]
        print(p,np)
        if len(p) == 1 and sum(np)/len(np) >= 2*p[0]:
            c+=1
            print(True)
    
    print(c)