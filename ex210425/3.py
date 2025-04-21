def f(s1, s2, m):
    if m<0: return 0
    if s1+s2 >= 189: return m%2==0

    h = [f(s1+s2, s2, m-1), f(s1,s2+s1, m-1), f(max(s1,s2),max(s1,s2),m-1)]

    if (m-1)%2==0: return any(h)
    else: return all(h)

def g(s1, s2, m):
    if m<0: return 0
    if s1+s2 >= 189: return m%2==0

    h = [g(s1+s2, s2, m-1), g(s1,s2+s1, m-1), g(max(s1,s2),max(s1,s2),m-1)]

    if (m-1)%2==0: return any(h)
    else: return any(h)

print(19, min([s for s in range(1,184) if g(5,s,2)]))
print(20, [s for s in range(1,184) if not f(5,s,1) and f(5,s,3)])
print(21, min([s for s in range(1,184) if f(5,s,4) and not f(5,s,2)]))
