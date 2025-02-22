def ispal(n):
    for i in range(len(str(n))//2):
        if str(n)[i]!=str(n)[len(str(n))-1-i]:
            return False
    return True

def f(x,q):
    a = []

    while x>0:
        a+=[x%q]
        x//=q
    return a[::-1]

c = 0

for x in range(15,7**7,16):
    x5 = f(x,5)

    k = [i for i in set(x5) if x5.count(i) % 2 == 1]

    if len(k) <= 1:
        c+=1

print(c)