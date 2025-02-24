from fnmatch import fnmatch
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5878.txt') as f:
    s = f.readline()
    for i in 'ABCDEF':
        for j in range(51,2,-3):
            s = s.replace(i*(j+2), i*j + ' ' + i*j)
            s = s.replace(i*(j+1), i*j + ' ' + i*j)
            s = s.replace(i*j, '*'*j)
    for i in 'ABCDEF':
        s = s.replace(i, ' ')
    a = [len(x) for x in s.split()]
    print(max(a))