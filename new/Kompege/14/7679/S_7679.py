import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from string import ascii_uppercase

alf = '0123456789' + ascii_uppercase

ans = []

for x in alf[:20]:
    for y in alf[:11]:
        for t in alf[:8]:
            try:
                ans.append( 
                (int(f'1{x}{y}',20) + int(f'3{y}',11))/
                (int(f'4{y}', 11)  - int(f'{t}1', 8))
            )
            except:
                continue

print(max([x for x in ans if x%5 == 0]))