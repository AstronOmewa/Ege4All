import os

os.chdir(os.path.dirname(__file__))

with open('2.txt') as f:
    a = [tuple(map(int, l.split())) for l in f.readlines()]
    c = 0
    for i in range(len(a)):
        line = a[i]
        p = [x for x in line if line.count(x)>1]
        np = [x for x in line if line.count(x)==1]



        if len(np)==4 and p[0]>=sum(np)/len(np):
            print(i+1)
            break

