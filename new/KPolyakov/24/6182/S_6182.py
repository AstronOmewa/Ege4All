import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6182.txt') as f:
    s = f.readline()

    s = s.replace('A', 'A A').replace('D', 'D D')

    a = [len(x) for x in s.split() if x[0] in 'AD' and x[-1] in 'AD' and x[0]!=x[-1]]
    print(max(a))