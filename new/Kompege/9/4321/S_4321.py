import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.4321.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]
    c = 0
    for l in ls:
        l = sorted(l)
        if l[0]**3+l[1]**3 > (l[2] + l[3]+l[4])**2:
            c+=1
    print(c)