def int190(x):
    r = 0
    for i in range(len(x)):
        r+=(190**(len(x)-i-1))*int(x[i],36)
    
    return r

m = []

for x in range(190):
    for y in range(190):
        a1 = int('n',36)*190**2+x*190+int('w',36)
        a2 = int('y',36)*190**3+y*190**2+int('a',36)+int('r',36)
        s = a1+a2
        if s%189 == 0:
            m.append((x*y, (s) // 189))

print(max(m))