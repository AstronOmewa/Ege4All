import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.6406.txt') as f:
    #поменяли в файле A->1, B->2

    n, l, m = map(int,f.readline().split())

    a = [tuple(map(int, x.split())) for x in f]

    a.sort()
    print(a[-10:])
    park = [0]*(n + l) #[0-l) - легковые, [l - l+m) - автобус

    ans1, ans2 = 0, 0

    for x in a:
        s, t, p = x

        #легковые
        if p == 1:
            for i in range(len(park)):
                if park[i] <= s:
                    park[i] += t
                    break
            else: 
                ans2+=1
        # автобусы
        else:
            for i in range(l,l+m):
                if park[i] <= s:
                    park[i] += t
                    break

        
    print(ans1, ans2)