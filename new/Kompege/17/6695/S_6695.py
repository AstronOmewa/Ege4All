import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

a = [*map(int, open('17.6695.txt'))]

ps = [x+y for x, y in zip(a, a[1:]) if abs(x)>abs(y) and (x+y)%27 == 0]

print(len(ps), abs(min(ps)))