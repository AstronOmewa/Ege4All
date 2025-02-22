for x in range(401,10000):
    n = hex(16**560+16**120-x)[2:]

    if n.count('0') == 442:
        print(x)
        break