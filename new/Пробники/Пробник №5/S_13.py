from ipaddress import *

ip1, ip2 = '176.213.225.119', '176.213.195.58'

for m in range(16,31):
    ipnet1, ipnet2 = [str(x) for x in ip_network(f'{ip1}/{m}',0)],\
    [str(x) for x in ip_network(f'{ip2}/{m}',0)]
    if ip1 not in ipnet2 and ip2 not in ipnet1:
        print(m)

print(int('11100000',2))