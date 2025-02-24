import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.5829.txt','r') as f:
    print(f.readline())