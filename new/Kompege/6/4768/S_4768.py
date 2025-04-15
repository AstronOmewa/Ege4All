# import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# from turtle import *
# from itertools import *

# k = 100
# lt(90)
# pd()
# tracer(0)

# coords =set()

# for n in range(100):
#     up()
#     fd(10*k)
#     down()
#     dot(3,'red')
#     coords.add((int(xcor()),int(ycor())))
#     up()
#     rt(180)
#     fd(10*k)
#     down()
#     dot(3,'red')
#     coords.add((int(xcor()),int(ycor())))
#     up()
#     rt(198)

# canvas = getcanvas()
# c = 0

# for x, y in product(range(-200,200), repeat=2):
#     if canvas.find_overlapping(x*k, y*k, x*k, y*k)!=():
#         c+=1

# print(len(coords)-1)
# exitonclick

import turtle
import math

# Функция для перемещения Черепахи и рисования
def draw_turtle_path():
    turtle.setpos(10, 15)  # Начальная позиция
    turtle.setheading(90)   # Направление вверх
    turtle.pendown()  # Опускаем хвост

    for _ in range(15):  # Повторяем 15 раз
        for _ in range(20):  # Внутренний цикл на 20 повторений
            turtle.forward(40)  # Вперед 40
            turtle.right(90)  # Направо 90
        turtle.left(90)  # Налево 90

    turtle.penup()  # Поднимаем хвост
    turtle.hideturtle()

# Функция для поиска точек внутри контура
def count_integer_points():
    # Получаем текущие координаты всех точек, которые нарисовала черепаха
    turtle_points = turtle.getscreen().getcanvas().find_all()

    # Максимальные координаты для перебора
    min_x = 10  # Начальная позиция по x
    max_x = 10  # Это значение будет обновляться в дальнейшем
    min_y = 15  # Начальная позиция по y
    max_y = 15  # Это значение будет обновляться в дальнейшем

    # Сохраняем все точки, которые нарисованы
    drawn_points = set()
    for point in turtle_points:
        coords = turtle.getscreen().getcanvas().coords(point)
        if coords:
            drawn_points.add((round(coords[0]), round(coords[1])))

            # Обновляем границы
            x, y = round(coords[0]), round(coords[1])
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

    # Подсчитываем точки с целочисленными положительными координатами внутри контура
    count = 0
    for x in range(min_x + 1, max_x + 1):
        for y in range(min_y + 1, max_y + 1):
            if (x, y) not in drawn_points:
                count += 1

    return count

# Главный код
turtle.speed(0)  # Установить максимальную скорость
draw_turtle_path()  # Рисуем путь Черепахи
turtle.done()  # Завершаем рисование

# Получаем количество точек
result = count_integer_points()
print("Количество точек с целочисленными положительными координатами, которые лежат внутри полученного контура и при этом не лежат на оставленном черепахой следе:", result)
