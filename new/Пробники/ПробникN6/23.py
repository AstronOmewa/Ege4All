fi = [1,1,2,3,5,8,13,21]

def closestfigt(x):
    fidif = [f-x for f in fi]
    return fi[fidif.index(min(x for x in fidif if x > 0))]

def f(x,y):
    if x>y: return 0
    if x==y: return 1
    return f(x+1,y)+f(x+4,y)+f(closestfigt(x),y)

print(f(1,13))
