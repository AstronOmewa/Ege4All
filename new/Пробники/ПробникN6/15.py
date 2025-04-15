for a in range(1,1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+3*x) < a) or (x>9) or (y>20)):
                flag = False
                break
        if not flag:
            break
    if not flag:
        continue

    print(a)