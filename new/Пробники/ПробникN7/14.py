def conv(x, toa):
    a = ''
    while x>0:
        a+=str(x%toa)
        x//=toa
    return a[::-1]

print(conv(3*16**8-4**5+3,4).count('3'))