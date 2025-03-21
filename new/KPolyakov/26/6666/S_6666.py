import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.6666.txt') as f:
    n, k, m = map(int, f.readline().split())

    a = [tuple(map(int, x.split())) for x in f]

    a.sort(key = lambda x: (x[0], -x[1]))

    train = [0]*m
    ans1 = ans2 = 0
    for x in a:
        s, e = x
        if train[s] < k:
            ans1+=1
            for i in range(s,e):
                train[i] += 1
    ans2 = len([x for x in train if x == k])

    print(ans1, ans2)


