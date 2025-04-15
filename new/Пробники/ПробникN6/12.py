s = '8'*9 + '5'*(21-9)

while '555' in s or '888' in s:
    while '555' in s: s = s.replace('555', '8')
    while '888' in s: s = s.replace('888', '5')

print(s)