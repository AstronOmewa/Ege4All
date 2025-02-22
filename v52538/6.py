from turtle import *

screensize(2000,2000)
tracer(0)
pd()
x, y, k = -40, -20, 20
for i in range(10):
    goto(x + 6*k, y + 15*k)
    x, y = x + 6*k, y + 15*k
    goto(x + 4*k, y - 6*k)
    x, y = x + 4*k, y - 6*k
    goto(2*k,2*k)
    goto(2*k+ 3*k, 2*k+9*k)
    x, y = 2*k + 3*k, 2*k+9*k

pu()

from itertools import *

for x, y in product(list(range(-30,30)), repeat= 2):
    goto(x*k,y*k)
    dot(4, 'blue')
done()
# ans : 15