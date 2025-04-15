from ipaddress import *

def fillwith0(x):
    return '0'*(8-len(x))+x

for A in [int('1'*n+'0'*(8-n),2) for n in range(8)]:
    ipn = [str(x) for x in ip_network(f'243.46.4.198/255.255.{A}.0',0)]
    flag = True
    for x in ipn:
        bytes = [fillwith0(bin(int(r))[2:]).count('0') for r in x.split('.')]
        # print(bytes)
        if bytes[0]+bytes[1] <= bytes[2]+bytes[3]:
            flag = False
            break

    if flag: print(A)