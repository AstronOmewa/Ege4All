import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('17.6360.txt') as f:
    a = [int(x) for x in f.readlines()]

    min7 = min([x for x in a if (str(x)[-1])=='7'])
    c = 0
    maxs = 0

    for i in range(len(a) - 1):
        x, y = a[i], a[i+1]
        if (abs(x)%10)==(abs(y)%10) and (abs(x)%7 == 0)!=(abs(y)%7 == 0)\
            and x**2 + y**2 <= min7**2:
            c += 1
            maxs = max(maxs, x**2+y**2)

    print(c, maxs)