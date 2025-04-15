def tr(x):
    res = ''
    while x>0:
        res+=str(x%3)
        x//=3
    return res[::-1]

a = []

for i in range(11,1000):
    res = '22'+tr(i) 
    if str(i).count('0')+str(i).count('2')>str(i).count('1'):
        pass
    else:
        res = '11'+tr(i)
    res = int(res,3)
    if res > 100:
        a.append(res)

print(min(a))