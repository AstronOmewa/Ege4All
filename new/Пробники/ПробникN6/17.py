import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('17.txt') as f:
    a = [int(x) for x in f.readlines()]

    c = 0

    ma = [x for x in a if x%22 == 0]
    ma = sum(ma)/len(ma)
    ms = 0

    for i in range(len(a)-1):
        maxa1 = (oct(a[i])[2:]).index(str(max(int(x) for x in oct(a[i])[2:])))
        mina1 = (oct(a[i])[2:]).index(str(min(int(x) for x in oct(a[i])[2:])))
        maxa2 = (oct(a[i+1])[2:]).index(str(max(int(x) for x in oct(a[i+1])[2:])))
        mina2 = (oct(a[i+1])[2:]).index(str(min(int(x) for x in oct(a[i+1])[2:])))
        if (a[i]+a[i+1] < ma) and (maxa1 < mina1) and (maxa2 < mina2):
            c+=1
            ms = max(ms, a[i]+a[i+1])

    print(c, ms)