def f(x,y):
    if x==y:
        return 1
    if x>y or x==18:
        return 0
    
    return f(x*3,y)+f(x+2,y)

print(f(4,46)*f(46,52))