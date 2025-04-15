def f(x,a):
    return ((x%2==0) <= (not (x%5==0))) or (x+a >= 70)

for a in range(1000):
    if all(f(x,a) for x in range(1000)):
        print(a)
        break