def g(s1, m):
    if s1<20:
        return (m)==0 # <--- работает в этой задаче потомучо
    
    if m == 0:
        return 0
    
    h = [g(s1-10, m-1), g(s1//2, m-1)]

    if (m-1)%2 == 1:
        return any(h)
    else:
        return all(h)
    
print(max([s for s in range(31, 300) if not g(s,1) and g(s,3)]))
print([s for s in range(31,300) if g(s,4) and not g(s,2)])
print([s for s in range(31,300) if g(s,5) and not g(s,3) and not g(s,1)])