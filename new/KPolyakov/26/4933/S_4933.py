import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.4933.txt') as f:
    n = int(f.readline())
    a = [tuple(map(int, x.split())) for x in f]

    a.sort()
    
    bus = [0]*10**6

    for x in a:
        s, e = x
        for i in range(s,e):
            bus[i] += 1

    ans1, ans2 = max(bus), len([x for x in bus if x>0])
    print(ans1, ans2)