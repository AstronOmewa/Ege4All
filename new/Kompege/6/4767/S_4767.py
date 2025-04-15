import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from turtle import *
from itertools import product

z = 20
lt(90)
speed(1000)

for i in range(38):
    fd(10*z)
    dot(4)
    rt(180)
    fd(10*z)
    dot(4)
    rt(190)
    
done()