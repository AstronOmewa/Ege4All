import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ispr(x):
    if x<0: return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

a = [*map(int, open('17.9993.txt'))]
d = max([t for t in a if abs(t)%100==17])
ps = [x*y for x,y in zip(a,a[1:]) if (x+y)%d==0 and ispr(x)!=ispr(y)]

print(len(ps), max(ps))