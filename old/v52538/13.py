from ipaddress import *

n = [f'{x:b}' for x in ip_network('90.65.32.0/255.255.224.0', 0)]
c = 0

print(n[2:])
for x in n:
    if x.count('1') == x.count('0'):
        c += 1

print(c)
# ans : 715