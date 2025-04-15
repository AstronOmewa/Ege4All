import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from itertools import product
from turtle import *

screensize(2000,2000)
speed(1000)
lt(90)
k=100
pd()
rt(45)

color('red','blue')

begin_fill()
for i in range(4):
    fd(55*k)
    rt(90)
end_fill()

canvas = getcanvas()
c = 0
for x,y in product(range(-200,200),repeat=2):
    if canvas.find_overlapping(x*k,y*k,x*k,y*k)==(5,):
        c+=1

print(c)

exitonclick()