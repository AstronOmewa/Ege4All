import os

os.chdir(os.path.dirname((os.path.abspath(__file__))))

with open('24-241.txt', 'r') as file:
    s = file.readline().strip()

    n = len(s)
    left = 0
    max_len = 0

    # Ищем первую 'O' для left
    while left < n and s[left] != 'O':
        left += 1

    for right in range(left, n):
        if s[right] == 'O':
            # Проверяем все промежутки между 'O' в s[left..right]
            valid = True
            prev_o = left
            for i in range(left + 1, right + 1):
                if s[i] == 'O':
                    # Подсчитываем 'F' между prev_o и i
                    f_count = s[prev_o + 1:i].count('F')
                    if f_count > 2:
                        valid = False
                        break
                    prev_o = i
            if valid:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
            else:
                # Сдвигаем left до следующей 'O'
                left += 1
                while left < n and s[left] != 'O':
                    left += 1

    print(max_len)