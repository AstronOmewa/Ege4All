import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('26.7015.txt') as f:
    n, k = map(int, f.readline().split())

    meters = [0]*(k-1)

    a = sorted([(int(l.split()[0]), int(l.split()[1])) for l in f.readlines()[1:]], key = lambda x: x[0])

    mr, cur = 0, 0
    ans1 = ans2 = 0
    while cur < k:
        
        cr = a[cur][1]
        while cur < n and a[cur][0] <= mr+1:
            if a[cur][0]<=k and a[cur][1] >= k: ans2+=1
            cr = max(cr, a[cur][1])
            cur += 1
        mr = cr
        k+=1
    print(n - ans1, ans2)