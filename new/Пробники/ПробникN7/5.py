for i in range(100,10**5):
    k = int(bin(i)[2:][::-1],2)
    if k == 9:
        print(i)
        break