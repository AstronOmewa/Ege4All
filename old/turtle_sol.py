# from turtle import *
# from itertools import *

# tracer(0)

# pendown()
# k = 35
# screensize(2000,2000)

# for i in range(4):
#     fd(14*k)
#     rt(90)
# for i in range(5):
#     fd(5*k)
#     rt(45)

# penup()

# for x, y in product(list(range(-20,20,1)),repeat=2):
#     goto(x*k, y*k)
#     dot(3, 'blue')

# done()


from turtle import *
from itertools import *

tracer(0)

pendown()
k = 35
screensize(2000,2000)

for i in range(2):
    fd(9*k)
    rt(90)
    fd(15*k)
    rt(90)
penup()
fd(12*k)
rt(90)
down()
for i in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)

penup()

for x, y in product(list(range(-20,20,1)),repeat=2):
    goto(x*k, y*k)
    dot(5, 'blue')
    dot(2, 'white')

done()