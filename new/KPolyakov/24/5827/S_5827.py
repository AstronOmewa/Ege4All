from string import ascii_uppercase
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5827.txt') as f:
    s = f.readline()

    for x in ascii_uppercase:
        s = s.replace(x, ' ')

    s = s.split()

    a = [int(x) for x in s if x[0]!='0']
    print(max(a))
    