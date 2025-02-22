def f(x,a):
    return ((x%2 == 0) <= (not (x%3 == 0))) or ((x + a )>= 80)

for a in range(1,1000):
    fl = True
    for x in range(1,10000):
        if f(x, a) != 1:
            fl = False
            break
    
    if fl == True:
        print(a)
        break

# ans : 74