def a(x):
    if x%2 == 0:
        x /= 2
    else:
        x -= 1

    if x%3 == 0:
        x /= 3
    else:
        x -= 1
    
    if x%5 == 0:
        x /= 5
    else:
        x -= 1

    return x

c = 0

for x in range(10**6):
    if a(x) == 3:
        c+=1

print(c)