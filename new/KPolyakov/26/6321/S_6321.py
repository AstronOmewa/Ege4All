import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.6321.txt') as f:
    n,m = map(int, f.readline().split())
    a = [tuple(map(int, x.split())) for x in f]

    a.sort(key = lambda x: x[0])
    # print(a[10:])

    bank = [0]*n
    bank_c = [0]*n 
    ans1, ans2= 0,0

    for x in a:
        s, t = x
        for i in range(n):
            if bank[i] <= s and s<=1440: 
                bank_c[i]+=1
                bank[i] = s + t
                if i == 2:
                    ans2 = s
                break
        # queue:
        else:
            mint = min(bank)
            ib = bank.index(mint)

            if mint<=1440: 
                ans1 = max(ans1, mint - s)
                bank[ib] += t
                bank_c[ib] += 1
                if ib == 2:
                    ans2 = mint

    print(ans1, ans2) # 1 запуск - определение самого посещаемого банкомата. 2 запуск - ответ на вопрос задачи с учетом, что наиболее посещаемый - второй