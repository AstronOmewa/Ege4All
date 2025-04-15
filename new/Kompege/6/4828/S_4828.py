import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from turtle import *
from itertools import product
speed(1000)
z = 10
color('red','blue')
begin_fill()
for i in range(1):
    goto(xcor()+5*z,ycor()+15*z)
    goto(xcor()+111*z,ycor()+0*z)
    goto(xcor()-60*z,ycor()-15*z)
    goto(xcor()-56*z,ycor()+0*z)
end_fill()

cumvas = getcanvas()
c = 0

for x, y in product(range(-200,200),repeat=2):
    if cumvas.find_overlapping(x*z, y*z, x*z, y*z) == (5,):
        print(cumvas.find_overlapping(x*z, y*z, x*z, y*z))
        c+=1
print(c)
exitonclick()