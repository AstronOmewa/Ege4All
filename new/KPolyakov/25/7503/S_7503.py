import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def m(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return i + n//i
    return 0

a = []

for n in range(1_000_000, 0, -1):
    if m(n)%100 == 18 and len(a)<5:
        a.append((n, m(n)))

print(*sorted(a), sep = '\n')