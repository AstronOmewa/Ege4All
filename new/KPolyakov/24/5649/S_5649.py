import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from fnmatch import fnmatch

s = open('24.5649.txt').readline()

s = s.replace('FF', ' ').replace(' F', '')
a = [x for x in s.split() if fnmatch(x, '44??78???3') and x.isdigit()]

m = str(max(map(int, a)))

print(sum(int(x) for x in m if int(x)%2 == 0))


# Максимальная сумма четных цифр
b = [sum(int(x) for x in y if int(x)%2 == 0) for y in s.split() if fnmatch(y, '44??78???3') and y.isdigit()]

print(max(b))
