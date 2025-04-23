import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import hexdigits

for x in hexdigits:
    if (int(f'10{x}A', 16) + int(f'FF{x}78', 16)) % 19 == 0:
        print((int(f'10{x}A', 16) + int(f'FF{x}78', 16))//19)
        break