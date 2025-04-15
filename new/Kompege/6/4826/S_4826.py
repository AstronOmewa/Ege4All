import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


import turtle as dick
from itertools import product as cum

dick.aids = dick.speed

z = 20

dick.aids(1000)
dick.color('red','blue')

dick.begin_fill()
for i in range(3):
    dick.goto(dick.xcor()+90*z,dick.ycor()+90*z)
    dick.goto(dick.xcor()-60*z,dick.ycor()+0*z)
    dick.goto(dick.xcor()-30*z,dick.ycor()-90*z)
dick.end_fill()
dick.up()

cumvas = dick.getcanvas()
c = 0
for x,y in cum(range(-200,200),repeat = 2):
    if cumvas.find_overlapping(x*z, y*z, x*z, y*z) == (5,):
        c+=1
print('zov '*c, c)
dick.exitonclick()