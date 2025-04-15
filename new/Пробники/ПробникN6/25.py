def ap(n):
    n = sorted(n)
    return all((n[i+1]-n[i]) == (n[i]-n[i-1]) for i in range(1,len(n)-1))

def primedivs(n):
    m = n
    d = set()
    for i in range(2,int(n**0.5)+1):
        while m%i==0:
            m//=i
            d.add(i)

    return sorted(d)

a = set()

for x in range(100_000, 500_000+1):
    p = list(primedivs(x))
    if len(p)>3 and ap(p):
        a.add((x,len(p)*(p[1]-p[0])))
        print(p)

print(*sorted(a))