def f(n):
    return sum(int(x) for x in str(n))

def g(n):
    if n<10: return n
    else: return g(f(n))

print(sum(g(n) for n in range(10,100)))