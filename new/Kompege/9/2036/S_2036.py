import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('9.2036.txt') as f:
    ls = [tuple(map(int, l.split())) for l in f.readlines()]
    k = 0
    for l in ls:
        a,b,c = sorted([l[i] for i in range(3)])[::-1]
        if a+b+c==180 and a < 90:
            k += 1
    print(k)