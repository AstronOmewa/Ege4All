import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
a = set()
for x in range(10,67):
    for y in range(x):
        a.add(7*67**4+3*67**3+x*67**2+1*67+y +\
        4*x**3+9*x**2+y*x+6)

print(len(a))