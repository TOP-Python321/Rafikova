cell_1 = input('Введите координаты первой клетки: ')
cell_2 = input('Введите координаты второй клетки: ')

if ('a' <= cell_1[0] <= 'h' and '1' <= cell_1[1] <= '8' and
    'a' <= cell_2[0] <= 'h' and '1' <= cell_2[1] <= '8'):
    if cell_1[0] == cell_2[0] or cell_1[1] == cell_2[1]:
        print('да')
    else:
        print('нет')
else:
    print('Ошибка, некорректный ввод')
    
# Введите координаты первой клетки: d4
# Введите координаты второй клетки: e4
# да

# Введите координаты первой клетки: a2
# Введите координаты второй клетки: c4
# нет