import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from turtle import *
from itertools import product
screensize(2000,2000)
speed(5000)
z = 10
color('red','blue')
goto(10*z, 15*z)

lt(90)
points = set()
begin_fill()
for i in range(4):
    
    for j in range(4):
        fd(40*z)
        rt(90)
        points.add((int(xcor()),int(ycor())))
    lt(90)
    
end_fill()
canvas = getcanvas()
for x, y in product(range(1,200), repeat=2):
    if canvas.find_overlapping(x*z, y*z, x*z, y*z) == (5, ):
        pass
print(len(points))
exitonclick()