import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.1.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
    a.sort()
    c, maxs = 0, 0

    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if ((a[i]+a[j]) in a) and (a[i]%2)==(a[j]%2):
                c+=1 
                maxs = max(maxs, a[i]+a[j])
    
    print(c, maxs)