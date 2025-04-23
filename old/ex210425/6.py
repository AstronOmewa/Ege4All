from fnmatch import fnmatch
from itertools import product
# 2?1?2?1?2?1

def tr(x):
    a = ''
    while x>0:
        a += str(x % 3)
        x //= 3
    return a[::-1]

ans = []

for a1, a2, a3, a4, a5 in product('012', repeat = 5):
    if int(f'2{a1}1{a2}2{a3}1{a4}2{a5}1', 3)%148 == 0:
        ans.append((int(f'2{a1}1{a2}2{a3}1{a4}2{a5}1', 3), \
                    int(f'2{a1}1{a2}2{a3}1{a4}2{a5}1', 3)//148))

print(*sorted(ans)[::-1])
print([(tr(a),b*148) for (a,b) in ans])

print(9960/4)