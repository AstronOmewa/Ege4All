import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

a = [*map(int, open('17.3370.txt'))]
s = sum([int(str(abs(t))[0]) for t in a])
ps = [x+y for x,y in zip(a, a[1:]) if x*y > s]
print(len(ps), max(ps))