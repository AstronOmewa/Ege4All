import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.2101.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]
    t = 0

    for l in ls:
        a,b,c = sorted(l)[::-1]
        print(a,b,c)
        if c**2<a**2+b**2 and a**2<b**2+c**2 and b**2<c**2+a**2: t+=1

    print(t)