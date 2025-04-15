from itertools import *
def g(a,b,c,d):
    return (abs(a-b) == abs(c-d)) or (abs(a-c) == abs(b-d)) or (abs(a-d)==abs(b-c))
with open('9.txt') as f:
    s = [list(map(int, x.split())) for x in f.readlines()]
    c = 0
    for l in s:
        if (max(l) + min(l))%3 == 0 and g(l[0],l[1],l[2],l[3]):
            c+=1
            print(*l)
    print(c)