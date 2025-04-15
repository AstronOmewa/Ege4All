import os

os.chdir(os.path.dirname((os.path.abspath(__file__))))

def ispal(x):
    return str(x)==str(x)[::-1]

with open('17-328.txt') as f:
    l = [int(x) for x in f.readlines()]
    max50 = max(x for x in l if x%50 == 0)

    k, maxs = 0, 0

    for i in range(len(l)-2):
        a, b, c = l[i], l[i+1], l[i+2]

        if ispal(a+b) and ispal(a+c) and ispal(b+c) and max(a+b,a+c,b+c)<max50:
            k+=1
            maxs = max(maxs, a+b+c)
            print(i,a+b,a+c, b+c, a+b+c<max50)
    print(k, maxs)
    print(ispal('1212'), len(l))