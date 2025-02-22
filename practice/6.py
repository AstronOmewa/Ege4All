from turtle import *
k = 10

# # # forward(1*k)
# # fd(1*k)
# # # back(1*k)
# # bk(1*k)
# # # left(60)
# # left(60)
# # # right(60)
# # right(60)
# # прорисовка с макс скоростью
# # speed(0)
# # # прорисовка без показа
# # tracer(0)
# # update()
# # # размер экрана
# # screensize(10_000,10_000)
# # # считать текущие значения координат
# # xcor(),ycor() == (0,0)
# # # показать холст, не закрывая
# # done()
# # # переход к (x*k, y*k)
# # goto(x*k, y*k)
# # # точка размера 1px красного цвета в текущей координате
# # dot(size=1, color='red')
# # # опустить хвост, поднять хвост
# # down()
# # up()

# k = 10

# left(90)
# tracer(0)
# screensize(10000,10000)

# up()
# # for x,y in enumerate(range(10*k)):
# #     goto(x*k, y*k)
# #     dot(2,'red')
# # down()

# # for i in range(9):
# #     fd(12*k)
# #     rt(90)
# #     fd(6*k)
# #     rt(90)
# # up()
# # fd(1*k)
# # rt(90)
# # fd(3*k)
# # lt(90)
# # down()

# # for i in range(9):
# #     fd(53*k)
# #     rt(90)
# #     fd(75*k)
# #     rt(90)

# # up()
# # tracer(0)
# # for x in range(-10,20):
# #     for y in range(-20,30):
# #         goto(x*k, y*k)
# #         dot(3,'red')
# update()
# done()

# '''

# '''

# lt(90)

# rt(45)

# for _ in range(10):
#     rt(45)
#     fd(203)
#     rt(45)

# up()

# bk(40)
# rt(45)

# down()

# for i in range(5):
#     fd(20)
#     lt(90)
screensize(10_000, 10_000)
tracer(0)
k = 20 
x,y = 0,0

for i in range(10):
    dx, dy = (6,15)
    goto(x+6*k, y+15*k)
    x,y = x+dx*k, y+dy*k
    

    dx, dy = (4,-6)
    goto(x+4*k, y-6*k)
    x,y = x+dx*k, y+dy*k

    goto(2*k, 2*k)
    x,y = (2*k, 2*k)

    dx, dy = (3,9)
    goto(x+3*k, y+9*k)
    x,y = x+dx*k, y+dy*k

update()

up()
tracer(0)
for x in range(-10,50):
    for y in range(-20,50):
        goto(x*k, y*k)
        dot(3,'red')

done()