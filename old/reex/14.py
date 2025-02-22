P = range(5,55)
Q = range(50,94)

def f(x, A):
    return (x not in P) and (x in Q) <= (x > A)

for A in range(-200,2000):
    if ([f(x, A) for x in range(0,300)].count(0)) == 20:
        print(A)
        break