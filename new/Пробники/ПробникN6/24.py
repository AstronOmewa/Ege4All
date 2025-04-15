from string import  ascii_uppercase
with open('24.txt') as f:

    s = f.readline()

    for x in ascii_uppercase:
        s = s.replace(x, 'A')
    s = s.split('A')
    
    num = [int(x) for x in s if x!='' and x[0]!='0']

    print(max(num))