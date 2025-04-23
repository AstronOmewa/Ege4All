import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('17.5882.txt') as f:
    a = [int(x) for x in f.readlines()]

    mina = min([min(x, y) for x,y in zip(a, a[1:]) if (abs(x)%10==3)!=(abs(y)%10==3)])
    s = sum(list(map(lambda x: int(x)**2, str(abs(mina)))))

    c = [x for x in a if '3' in str(x) and x >= s]

    print(len(c), min(c))