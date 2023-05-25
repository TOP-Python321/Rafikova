num_list = []
while True:
    num = int(input('Введите число: '))
    if num % 7:
        break    
    num_list.append(num)

print(*num_list[::-1])

# num_list += [num] в этом случае каждый раз будет создаваться новый объект с новым id, думаю что лучше использовать метод append()
# КОММЕНТАРИЙ: конкатенация списков быстрее выполняется, но в результате объект списка пересоздаётся (получает новый id); поэтому изменяющий, но не пересоздающий объект метод append() применяют там, где важно сохранить один и тот же объект (в основном при работе с собственными классами, дочерними от list)


# Введите число: 7
# Введите число: 14
# Введите число: 21
# Введите число: 23
# 21 14 7  


# ИТОГ: отлично — 3/3
