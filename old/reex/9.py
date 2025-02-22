from math import gcd

def t(x,y, h):
    if x==y and all(gcd(h[i],h[i+1])==1 for i in range(len(h)-1)):
        return 1
    if x > y or any(gcd(h[i],h[i+1])!=1 for i in range(len(h)-1)):
        return 0

    return t(x+1, y, h+[x]) + t(x+3, y, h+[x]) + t(x+7, y, h+[x])

print(t(12,31,[31]))