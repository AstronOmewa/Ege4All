import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

c=0

for x in range(8**10,16**8):
    if x%10 == 5:
        c+=1

print(c)