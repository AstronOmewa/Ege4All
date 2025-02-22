def maxd(n):
    for  i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return n//i
        
    return n

a = []

for x in range(10):
    for y in ['']+list(range(1000)):
        if int(int(f'3{y}52{x}',10)**0.5)==int(f'3{y}52{x}')**0.5:
            a.append((int(f'3{y}52{x}'),maxd(int(f'3{y}52{x}'))))

print(*sorted(a)[::-1], sep='\n')