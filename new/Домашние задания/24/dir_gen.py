import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for x in range(1,28):
    if not os.path.isdir(f'{x}'):
        os.mkdir(f'{x}')