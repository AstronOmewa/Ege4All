from itertools import product

a = set()

for p in product('ЖАЛЕЙ', repeat = 5):
    p = ''.join(p)
    if p[0]!='Й' and p[-1]!='Й' and 'ЕЙ' not in p and 'ЙЕ' not in p and p.count('Й')<=1:
        a.add(p)
a = list(a)
print(a[:10], len(a))