import os
import re
import shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def redistribute_files(directory):
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory):
        print(f"Каталог {directory} не существует.")
        return

    # Проходим по всем файлам в каталоге
    for filename in os.listdir(directory):
        # Полный путь к файлу
        file_path = os.path.join(directory, filename)

        # Проверяем, что это файл, а не подкаталог
        if os.path.isfile(file_path):
            # Используем регулярное выражение для извлечения номера задачи
            match = re.match(r'^(S_|Q_|\d{2}.)(\d+)', filename)
            if match:
                task_type = match.group(1)  # Тип задачи (S, Q, N)
                task_number = match.group(2)  # Номер задачи

                # Создаем имя подкаталога на основе номера задачи
                subdirectory_name = f"{task_number}"
                subdirectory_path = os.path.join(directory, subdirectory_name)

                # Создаем подкаталог, если он еще не существует
                if not os.path.exists(subdirectory_path):
                    os.makedirs(subdirectory_path)

                # Перемещаем файл в подкаталог
                new_file_path = os.path.join(subdirectory_path, filename)
                shutil.move(file_path, new_file_path)
                print(f"Файл {filename} перемещен в {subdirectory_path}")
            else:
                print(f"Файл {filename} не соответствует шаблону имени.")

def rename_subc(path):
    for filename in [name for name in os.listdir(".") if os.path.isdir(name)]:
        os.rename(f'{path}/{filename}',f'{path}/{''.join([x for x in filename if x.isdigit()])}')

# Укажите путь к каталогу с файлами
directory = os.path.dirname(os.path.abspath(__file__))
redistribute_files(directory)
rename_subc(directory)