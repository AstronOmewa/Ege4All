import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from turtle import *
x, y = 0, 0
k=5
screensize(2000,2000)
tracer(0)

for i in range(11):
    x, y = x+2*k, y+7*k
    goto(x,y)
    x, y = x-4*k, y-8*k
    goto(x,y)
    x, y = x+56*k, y-24*k
    goto(x,y)

up()
tracer(0)
from itertools import *
cvs = getcanvas()
c = 0
for x, y in product(range(-1000,1000), repeat=2):
    if cvs.find_overlapping(x*k,y*k,x*k,y*k) != ():
        c+=1 
print(c)
exitonclick()