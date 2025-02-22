# from itertools import product

# p = [x for x in product('01',repeat=16) if ''.join(x)[:3] == '101']

# q = [x for x in product('01',repeat=16) if ''.join(x)[-2:] == '01']

# a = set()

# for x in q:
#     if x not in p:
#         a.add(x)

# print(len(a))


# def f(s1,s2,m,fault=False):
#     if m<0: return 0
#     if (s1+s2)>=107:
#         if (s1+s2)<=170:
#             return m%2 == 0
#         else:
#             return m%2 == 1
        
#     h = [f(s1+10,s2,m-1),f(s1*2,s2,m-1),f(s1,s2+10,m-1),f(s1,s2*2,m-1)]

#     if (m-1)%2 == 0:
#         return any(h)
#     else:
#         if fault:
#             return any(h)
#         else: 
#             return all(h)
    

# print('19', min([s for s in range(1,101) if f(5,s,2,fault=True)]))
# print('20.1', [s for s in range(1,101) if f(5,s,3) and not f(5,s,2)])
# print('20.2', min([s for s in range(1,101) if f(5,s,3)]))
# print('21', [s for s in range(1,101) if f(5,s,4) and not f(5,s,2)])

# def f(b, e, hi='48 '):
#     ch = sum(hi.count(x) for x in ['2 ','4 ','6 ','8 ','0 '])
#     if b == e and ch==hi.count('5'):
#         return 1
#     elif b>=e:
#         return 0
    
#     return f(b+3,e," " + hi + " " + str(b)) + f(b - b%3 + 3,e," " + hi + " " + str(b)) + f(2*b+1,e," " + hi + " " + str(b))


# print(f(5,48))