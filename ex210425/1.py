from turtle import *

lt(90)
screensize(3000, 3000)
color('red','blue')
k = 15
tracer(0)
begin_fill()
for i in range(2):
    fd(7*k)
    rt(90)
    fd(12*k)
    rt(90)
end_fill()

up()
fd(7*k)
rt(90)
fd(12*k)
rt(90)

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
up()
# for x in range(-10,10):
#     for y in range(-10,10):
#         up()
#         goto(x*k,y*k)
#         down()
#         dot(3)

canvas = getcanvas()

c = 0
for x in range(-90,30):
    for y in range(-90,30):
        s = canvas.find_overlapping(x*k,y*k,x*k,y*k)
        print(s)
        if s!=():
            c+=1

print(c, 84*78+13*8-7*4)
done()