def ispr(n):
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    
    return True

for i in range(106732567, 152673836+1):
    x = i**0.25

    if int(i**0.25) == i**0.25 and ispr(int(x)):
        print(i,int(i**0.75))

