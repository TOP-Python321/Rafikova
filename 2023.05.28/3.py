from pathlib import Path
from utils import load_file


def ask_for_file() -> '< module >':
    
    """Запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file. Возвращает объект модуля, созданного при импортировании файла."""
    
    while True:
        path_input = Path(input(' Введите путь к файлу: '))
        if path_input.is_file():
            break
        else:
            print('! Ошибка, не существует файл по указанному пути !')
        
    return load_file(path_input)


# D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28>python -i 3.py
# >>> config_module = ask_for_file()
#  Введите путь к файлу: d:\student\2023.05.28\conf.py
# ! Ошибка, не существует файл по указанному пути !
#  Введите путь к файлу: D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data
# ! Ошибка, не существует файл по указанному пути !
#  Введите путь к файлу: D:\Лилия_мои_доки\Pythom_HW_git\Rafikova\2023.05.28\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
# >>>

# >>> module = ask_for_file()
#  Введите путь к файлу: d:\G-Doc\YandexDisk\Scripts\_Singles\si_unit.py
# >>>
# >>> module.SIUnit
# <class 'si_unit.SIUnit'>

# КОММЕНТАРИЙ: очень одобряю более гибкую реализацию функции load_file()


# ИТОГ: отлично — 6/6
