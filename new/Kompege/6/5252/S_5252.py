import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


from turtle import *
from itertools import *

tracer(0)
k = 15
lt(90)

for i in range(8):
    fd(10*k)
    rt(45)
up()
for x, y in product(range(-100,100), repeat = 2):
    goto(x*k, y*k)
    dot(3,'red')

exitonclick()

# [S] = [n a^2/ tan(180/8) / 4] = 482
print(482)