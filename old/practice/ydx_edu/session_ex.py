# from itertools import permutations
# g, sg = 'НСЧЧК', 'ООЕИ'
# s = set()
# for p in permutations(g+sg):
#     if not any((p[i] in g)==(p[i+1] in g) or (p[i] in sg)==(p[i+1] in sg) for i in range(len(p)-1)):
#         s.add(''.join(p))
# print(len(s))



# from itertools import *
# def f(x,y,z,w):
#     return (y == (not w)) <= ( not (w and (x == (x or (w <= z)))))


# for g,h,i,j,k,l,m,n,o,q in product([0,1], repeat=10):
#     t = [
#         (g,h,1,1),
#         (i,j,1,k),
#         (l,1,m,1),
#         (1,n,o,q)
#     ]

#     if len(t) != len(set(t)): continue

#     for p in permutations('xyzw'):
#         if [f(**dict(zip(p,r))) for r in t]==[0,0,0,1]:
#             print(*p, sep='')


# from string import ascii_uppercase

# p = 19
# alf = '0123456789'
# alf += ascii_uppercase[:p-len(alf)]

# def f(x,p):
#     alf = '0123456789'
#     alf += ascii_uppercase[:p-len(alf)]
    
#     s = ''

#     while x!=0:
#         s = s+str(alf[x%p])
#         x//=p
    
#     return s[::-1]

# def inv_f(s,p):
#     alf = '0123456789'
#     alf += ascii_uppercase[:p-len(alf)]

#     s=s[::-1]

#     r = 0

#     for i in range(len(s)):
#         r+=alf.index(s[i])*p**i

#     return r
    
# m = 0
# for x in alf:
#     if (inv_f(f'98897{x}21',19)+inv_f(f'2{x}923',19)) % 18 == 0:
#         m = max(m,(inv_f(f'98897{x}21',19)+inv_f(f'2{x}923',19))//18)

# print(m)



# from random import shuffle
# m = ''
# for h in range(100):
#     s = '1'*203+'2'
#     s = [x for x in s]
#     shuffle(s)
#     s = ''.join(s)

#     while ('111' in s) or ('222' in s):
#         if '111' in s: s = s.replace('111','22',1)
#         else: s = s.replace('222','11',1)

#     if len(s)>len(m):
#         m = s

# print(m)



# c=0
# msum = 0
# with open('practice/ydx_edu/17.txt') as f:
#     l = [int(x) for x in f.readlines()]

#     for i in range(len(l)-3):
#         tr = (l[i],l[i+1],l[i+2])

#         m13 = max(x for x in l if x%100 == 13)

#         if all([sum(len(str(x))==3 for x in tr)==2,sum(x for x in tr)<=m13]):
#             c+=1
#             msum = max(msum,sum(x for x in tr))


# print(c,msum)



# def f(s,m):
#     if s>=22: return (m)%2==0
#     if m<0: return 0

#     h=[]

#     if s%2 == 0:
#         h = [f(s+1,m-1),f(s+2,m-1)]
#     else:
#         h = [f(s+1,m-1),f(s+2,m-1),f(s*2,m-1)]

#     if (m-1)%2==0:
#         return any(h)
#     else:
#         return all(h)
    
# print('19',[s for s in range(2,22) if f(s,4) and not f(s,2)])
# print('20',[s for s in range(2,22) if f(s,3) and not f(s,1)])
# print('21',[s for s in range(2,22) if f(s,5) and not f(s,3)])



# def divs4s(n):
#     d = set()

#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             d.add(i)
#             d.add(n//i)
#     return d

# for i in range(1,10**6):
#     c=0
#     max4 = 0
#     for x in divs4s(i):
        
#         if str(x)[0]=='4':
#             c+=1
#             max4 = max(x, max4)
#     if c==24: 
#         print(i,max4)



# from ipaddress import *

# for m in range(16,33):
#     ipn1, ipn2 = [ str(x) for x in ip_network(f'101.96.170.244/{m}',0)], [str(x) for x in ip_network(f'101.96.126.212/{m}',0)]

#     if ("101.96.170.244" not in ipn2[1:-1]) and ('101.96.126.212' not in ipn1[1:-1]):
#         print(32-m)


from math import *

for i in range(10):
    i1 = ceil((163*i)/8) #bytes

    if 32768*i1//1024 <= 3264:
        print(2**i, 32768*i1//1024)
