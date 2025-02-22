from itertools import permutations, product

a = []

for w in product('ИНФОРМАТК', repeat=4):
    try:
        if sum(w[i] == "ПАТИ"[i] for i in range(4))==2:
            a.append(''.join(w))
    except:
        continue


print(a[:10], len(a))