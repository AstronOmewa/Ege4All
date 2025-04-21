import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sums = []

def f(x):
    a = ''
    while x>0:
        a+=str(x%5)
        x//=5
    return a[::-1]

for x in range(1,100):
    for y in range(1,100):
        a = (55+2*5**x)*5**x+55+5**y
        sums.append(sum([int(x) for x in f(a)]))
    
print(max(sums))