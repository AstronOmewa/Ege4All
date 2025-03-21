import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.6320.txt') as f:
    n,m = map(int, f.readline().split())
    a = [tuple(map(int, x.split())) for x in f]

    start, end = 600, 1320

    a.sort(key= lambda x: x[0])

    tr = [0]*n
    tr_c = [0]*n
    ans1, ans2 = 0,0
    for x in a:
        s,e = x
        for t in range(len(tr)):
            if s< tr[t] and start<=s and e<=end:
                tr[t] = e
                ans1 += 1
                ans2 = t+1
                break

    print(ans1, ans2)