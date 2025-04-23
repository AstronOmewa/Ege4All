import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sums = []
alf = '0123456789ABCDEF'

for x in alf:
    for y in alf:
        a = int(f'27A{x}23',16) + int(f'8{y}E5D2',16) 
        if (a%5)==0:
            # print(sum([int(x) for x in str(a)]))
            sums.append(int(x, 16)+int(y, 16))

print(max(sums))