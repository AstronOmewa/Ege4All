import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from tqdm import tqdm 
from turtle import *
from itertools import product
screensize(2000,2000)
speed(1000)
z = 5

color('red','blue')
up()
for i in range(20):
    circle(4*z)
    goto(xcor()+8*z,ycor())
    down()
    dot(5)
    up()
goto(xcor(),ycor()-12*z)
down()
dot(5)
up()
for i in range(10):
    circle(8*z)
    goto(xcor()-16*z,ycor())
    down()
    dot(5)
    up()
goto(xcor(),ycor()-14*z)
down()
dot(5)
up()
for i in range(15):
    circle(6*z)
    goto(xcor()+12*z,ycor())
    down()
    dot(5)
    up()

exitonclick()

# ans: 3