files_list = input(' Введите названия файлов через точку с запятой: ').split('; ')

files_list_new = []
files_dict = {}

for f in files_list:
    files_dict[f] = files_dict.get(f, 0) + 1
    # КОММЕНТАРИЙ: хорошо, что в один цикл пошли
    if files_dict[f] == 1:
        files_list_new.append(f)
    else:
        # ИСПРАВИТЬ: метод find() вызывается лишний раз — оптимизируйте
        index_occurrence = f.find(".")
        files_list_new.append(f[:index_occurrence] + "_" + f'{files_dict[f]}' + f[index_occurrence:])

print(*sorted(files_list_new), sep="\n")


# Введите названия файлов через точку с запятой: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz


# ИТОГ: очень хорошо, требуется немного доработать — 4/5
