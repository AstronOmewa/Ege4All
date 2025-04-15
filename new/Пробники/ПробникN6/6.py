import turtle


from turtle import *
k = 15
tracer(0)
lt(90)
backward(4*k)
pendown()
for i in range(8):
    forward(12*k)
    right(45)
    forward(7*k)
    right(45)
    forward(6*k)
    right(90)

update()

up()
tracer(0)
for x in range(1,20):
    for y in range(1,20):
        goto(x*k, y*k)
        dot(4, 'red')

exitonclick()