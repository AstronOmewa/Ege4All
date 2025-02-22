def a(n):
    b = f'{n:b}'
    for i in range(3):
        if b.count('0') == b.count('1'):
            b = b + b[-1]
        elif b.count('0') < b.count('1'):
            b = b + '0'
        else:
            b = b + '1'
    
    return int(b, 2)

for n in range(61,10000):
    if a(n)%2 == 0 and a(n)%4 != 0:
        print(n)
        break