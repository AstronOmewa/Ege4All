a = []

for i in range(10**2,10**3):
    x = str(i)
    if '0' in x: continue

    if all(int(x)%int(t) == 0 for t in x) and all(int(x[::-1]) % int(t) == 0 for t in x):
        a.append(i)

print(a[10:20],len(a))