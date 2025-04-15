from itertools import *

alf = sorted('ВОДОПАД')
gl = 'ОА'

a = []

for p in product(set(alf), repeat = 7):
    x = ''.join(p)
    if all(not (x[i] in gl and x[i+1] in gl) for i in range(len(x)-1)) and all([x.count(alf[i]) == alf.count(alf[i]) for i in range(len(alf))]): a.append(x)

print(len(set(a)), a[100:200])