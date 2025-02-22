from ipaddress import ip_network, IPv4Address

n = ip_network('123.206.97.128/255.255.255.224')
c=0
for x in n:
    if bin(int(x))[-3:] in ['101','010']:
        c+=1

print(c)