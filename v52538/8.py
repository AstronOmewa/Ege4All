from itertools import *
c = 0
for p in permutations('вайфу', r = 4):
    if p[0]!='й' and 'фв' not in ''.join(p) and 'вф' not in ''.join(p):
        c+=1

print(c) 
# ans : 68