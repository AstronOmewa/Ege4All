import os

os.chdir(os.path.dirname(__file__))

with open('7.txt') as f:
    ls = [int(x) for x in f.readlines()]
    c = 0

    min4 = min([x for x in ls if len(str(x)) == 4])
    min2 = min([x for x in ls if len(str(x)) == 2])
    
    minsum = 1e10
    for i in range(len(ls)-3):
        a,b,c = ls[i:i+3]
        rem711 = [x % 7 == min4 % 11 for x in [a, b, c]]
        rem53 = [x % 5 == min2 % 3 for x in [a, b, c]]

        if rem711.count(True) == 1 and rem53.count(True) == 1:
            c += 1
            minsum = min(sum([a,b,c]), minsum)

    print(c, minsum)