a = []

for i in range(200,300):
    s = '5'*i
    while '55555' in s:
        s = s.replace('55555','88',1)
        s = s.replace('888','555',1)
    a.append((s.count('5'), i, s))
        
print(a[:100],max(a, key = lambda x: x[0]))