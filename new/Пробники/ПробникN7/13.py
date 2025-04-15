from ipaddress import *

for a in range(0,256):
    try:
        ipn = [f'{x:b}' for x in ip_network(f'196.233.{a}.52/255.255.255.248',0)]
        print([(ip[0:8].count('1')+ip[8:16].count('1'),ip[16:24].count('1')+ip[24:32].count('1')) for ip in ipn])
        if all(ip[0:8].count('1')+ip[8:16].count('1')>ip[16:24].count('1')+ip[24:32].count('1') for ip in ipn):
            print(a)
            break
    except:
        continue