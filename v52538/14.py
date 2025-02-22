from string import ascii_lowercase
chr_a = [chr(x) for x in range(48,10001)]

alf = ''.join(chr_a)
print(alf[:10])
def convp10(x, p):
    r = 0
    x = x[::-1]
    for i in range(len(x)):
        r += chr_a.index(x[i])*p**i
    return r

for p in range(1000,10000):
    q = int(str(p)[::-1])

    if convp10('961', p) == convp10('169', q):
        print(p)
        break

# ans : 2998