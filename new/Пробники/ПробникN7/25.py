def isprime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0: return False
    return True
c, k = 0, 0
for i in range(2532000, 2532160+1):
    if isprime(i): c+=1
    if isprime(i) and i>=2532000 and k<5: print(k+1, i); k+=1