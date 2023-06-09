set_binary_nums = {'0', '1', 'b'}
inp_num = input(' Введите число: ')
set_inp_num = set(inp_num)

# КОММЕНТАРИЙ: ох, накрутили проверок... есть такой эмпирический способ оптимизации кода: каждый раз когда у вас возникает третий подряд уровень вложенности условий (and — это те же вложенные условия), задавайте себе вопрос: "точно-точно-точно нельзя проще?" — в 95–97% случаев окажется, что можно =)
if inp_num == 'b' or inp_num == '0b' or inp_num == '1b':
    print('Нет')
elif set_inp_num <= set_binary_nums and 'b' not in set_inp_num:
    print('Да')
elif (
       set_inp_num <= set_binary_nums
    and inp_num[0] != '1'
    and inp_num.count('b') == 1
    and (inp_num.index('b') == 1 or inp_num.index('b') == 0)
):   
    print('Да')
else:
    print('Нет')

# Убрала условие len(inp_num) >= 2: почему то всегда думала что 0 в двоичной это 00, а 1 - 01. век живи-век учись))
# КОММЕНТАРИЙ: это просто способ записи — в десятичной тоже можно записать 0123, но это же всё равно число сто двадцать три; или даты записываются 01.01.2023 — число-то не меняется от появления ведущего нуля, мы всё равно понимаем, что это первый день первого месяца

# ИСПОЛЬЗОВАТЬ: пожалуй, я просто оставлю здесь более короткий вариант, а вы его сами осмыслите и прокомментируете во время работы над ошибками:
# ответ: да действительно намудрила( спасибо ваш вариант понятен. 
# 1. Проверяем что срез inp_num[2:] содержит только 0 и 1.
# 2. Прописали Множество возможныъх вариантов для среза inp_num[:2], и проверяем

answer = 'нет'
if set(inp_num[2:]) <= {'0', '1'}:
    if inp_num[:2] in {'0', '1', '01', '10', 'b1', 'b0', '0b'}:
        answer = 'да'
print(answer)


# Введите число: 0101
# Да
# Введите число: b11
# Да
# Введите число: 0b11001
# Да
# Введите число: 1b0101
# Нет
# Введите число: 01
# Да
# Введите число: 11
# Да
# Введите число: 1
# Да
# Введите число: 0
# Да
# Введите число: 0b003b
# Нет


# ИТОГ: хорошо, но можно лучше — 2/3
