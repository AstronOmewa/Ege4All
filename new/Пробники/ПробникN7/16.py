def f(n):
    return n if n<2 else n%2 + 10*f(n//2)

for n in range(10**6+1,10**7,2):
    if f(n)==100000100001000100101:
        print(n)
        break

print(int('100000100001000100101',2))