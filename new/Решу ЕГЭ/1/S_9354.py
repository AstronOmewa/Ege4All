import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from itertools import permutations as p

sort = lambda x: dict([k, ''.join(sorted(v))] for k, v in sorted(x.items()))

y = lambda x, c: {c[k]: ''.join(map(lambda d: c[d], v)) for k, v in x.items()}

s = {'1': '24', '2': '146', '3': '56', '4': '1267', '5': '36',\
     '6': '23457', '7': '46'}

S = sort({'А': 'БВ', 'Б': 'АВ', 'В': 'АБДЕГ', 'Г': 'ВЕК', 'Д': 'ВЕ',\
     'Е': 'ДВГК', 'К': 'ЕГ'})
# Получаем номера городов
print([t for i in p('1234567') if (t:={k: v for k, v in zip(i, 'АБВГДЕК')}) if sort(y(s,t))==S][0])
# Вывод: {'3': 'А', '5': 'Б', '6': 'В', '2': 'Г', '7': 'Д', '4': 'Е', '1': 'К'}
#  В - 6 пункт; Е - 4 пункт Тогда В -> E == 20