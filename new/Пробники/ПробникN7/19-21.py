def f(s,m):
    if m<0: return 0
    if s>=30: return (m)%2==0

    h = [f(s+2,m-1),f(s+3,m-1),f(s*2,m-1)]

    if (m-1)%2==0: return any(h)
    else: return all(h)

print(19, min([s for s in range(1,30) if f(s,2)]))
print(20, len([s for s in range(1,30) if f(s,3) and not f(s,1)]))
print(21, ([s for s in range(1,30) if not f(s,2) and f(s,4)]))