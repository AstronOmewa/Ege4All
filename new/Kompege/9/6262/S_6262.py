import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.6262.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]

    c = 0

    for l in ls:
        l = sorted(l)
        if (len(set(l))!=len(l)) + ([x%2==1 for x in l].count(1)==3) == 1:
            c+=1

    print(c) 