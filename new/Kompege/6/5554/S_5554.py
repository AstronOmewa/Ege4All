import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# В сумме за 1 раз поворот на 200 градусов
# Тогда 360*k=200*n:

for n in range(1,10):
    if 200*n%360 == 0:
        print(n)
        break