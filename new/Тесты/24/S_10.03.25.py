import os
from itertools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 1

with open('24_1.txt') as f:
    s = f.readline()

    s = s.replace('AB','A B').replace('AC', 'A C').replace('BC', 'B C').replace('AA', 'A A').replace('BB', 'B B').replace('CC', 'C C')
    s = s.split(' ')

    print(max(len(x) for x in s))

# ans: 199



#2

with open('24_2.txt') as f:
    s = f.readline()

    s = s.replace('AB','_').replace('CB','_')
    l = r = m = 0

    for r in range(len(s)):
        if s[r]=='_':
            r+=1
        else:
            m = max(m, r - l)
            l = r

    print(m)

# ans: 66



# 3

with open('24_3.txt') as f:
    s = f.readline()

    for i in range(len(s)):
        if not s[i].isdigit():
            s = s.replace(s[i], ' ')

    s = s.split(' ')

    print(max(int(x) for x in s if x!='' and int(x)%2 == 0))

# ans: 39168781038 



# 4

# with open('24_4.txt') as f:
#     s = f.readline()

#     s = s.replace('4','a').replace('3','e')

#     l = r = m = 0
    
#     needed = 'yandex'
#     s = s.replace(needed,'_')

#     print(s[:50])

#     curr = s[0]
#     for r in range(1,len(s)):
#         if s[r] == '_'
        
# ans: ___



# 5

# with open('24_5.txt') as f:
#     s = f.readline()

#     r = l = m = 0
#     gl = 'AOUIEY'
#     counter = {
#         'A' : 0,
#         'O' : 0,
#         'Y' : 0,
#         'U' : 0,
#         'E' : 0,
#         'I' : 0,
#     }
#     c0 = counter
#     for r in range(len(s)):
#         if s[r] in gl:
#             gl[s[r]]+=1
#         if 2 in counter.values() or :
#             counter = c0
#             m = max(m, r - l)
#             r = l

