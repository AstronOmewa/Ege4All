# res = []
# for x in '0123456789ABCDEFG':
#     s1 = '5432' + x + '67'
#     s2 = '302' + x
#     s1 = int(s1, 17)
#     s2 = int(s2, 17)
#     if (s1 + s2) % 19 == 0:
#         res.append((s1 + s2) // 19)
# print(max(res))


# def f(n):
#     cifri = [int(x) for x in str(n)]
    
#     chetnie = sum(x for x in cifri if x%2==0)**2
#     raznost = (max(cifri)-min(cifri))**3

#     chetnie, raznost = max(chetnie, raznost), min(chetnie, raznost)
#     return str(raznost)+str(chetnie)

# for i in range(1000,10**4):
#     if f(i)=='4343':
#         print(i)
#         break

alf = '012'

def troit_ebat_silno(n):
    m = n
    r = ''
    
    while m!=0:
        r+=alf[m%3]
        m//=3

    return ''.join(sorted(r)[::-1])

r = []

for i in range(1,10**6):
    res = troit_ebat_silno(i)
    res += res[0]

    res = int(res, 3)

    if int(res)<1200:
        r.append(res)

print(max(r))


# def f(x): 
#     r34='' 
#     while x>0: 
#         r34+=str(x%4) 
#         x//=4 
#     r34=r34[::-1] 
#     summ=sum([int(x) for x in r34]) 
#     if summ%2==0: 
#         r34+=r34[:2] 
#     else: 
#         r34+='2' 
#         r34='0'+r34[1:] 
#         r34='1'+r34[1:] 
#     return int(r34,4) 

# r = []

# for n in range(5,9900): 
#     if f(n)>250: 
#         r.append(f(n))
# print(min(r))


