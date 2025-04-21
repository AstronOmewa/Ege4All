from turtle import *

lt(90)
screensize(2000, 2000)
color('red','blue')
k = 10
speed(1000)
begin_fill()
for i in range(2):
    fd(3*k)
    rt(90)
    fd(12*k)
    rt(90)
end_fill()
fd(3*k)
rt(90)
fd(12*k)
rt(90)
up()
fd(4*k)
rt(90)
fd(6*k)
lt(90)
down()
begin_fill()
for i in range(2):
    fd(83*k)
    rt(90)
    fd(77*k)
    rt(90)
end_fill()

# for x in range(-100,100):
#     for y in range(-90*k, 10*k, k):
#         pu()
#         goto(x,y)
#         pd()
#         dot(3)

canvas = getcanvas()

c = 0
for x in range(-100,100):
    for y in range(-100,100):
        s = canvas.find_overlapping(x*k,y*k,x*k,y*k)
        if s!=():
            c+=1

print(c)
done()