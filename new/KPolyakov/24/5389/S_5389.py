import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5389.txt') as f:
    s = f.readline().replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')

    s = s.replace('A11', '*').replace('A', ' ').replace('1', ' ')
    
    a = [len(a) for a in s.split()]

    print(max(a))