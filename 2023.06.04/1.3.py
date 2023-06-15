from random import randrange

def tree_generator() -> list:

    """Генерирует дерево с произвольным количеством веток и листьев. Возвразщает список с произвольной глубиной вложенности"""
    
    tree = []
   
    if randrange(2):
        tree += ['leaf'] * randrange(1,4) 
    else:        
        for _ in range(randrange(0,5)):
            tree.append(tree_generator())
    
    return tree



# >>> tree_generator()
# ['leaf', 'leaf', 'leaf']
# >>> tree_generator()
# ['leaf']
# >>> tree_generator()
# []
# >>> tree_generator()
# [['leaf', 'leaf']]
# >>> tree_generator()
# [[['leaf'], [['leaf']]], ['leaf'], [['leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf'], ['leaf', 'leaf'], ['leaf']]]
# >>> tree_generator()
# [[['leaf'], ['leaf', 'leaf'], [[[[[[['leaf']], ['leaf'], [['leaf', 'leaf', 'leaf'], [['leaf'], ['leaf'], ['leaf'], ['leaf']]]]], [[], ['leaf'], ['leaf'], [[], [[['leaf'], [[['leaf', 'leaf']], []], [[['leaf', 'leaf'], ['leaf'], ['leaf']], ['leaf', 'leaf'], ['leaf'], ['leaf']]], ['leaf'], ['leaf', 'leaf', 'leaf']], ['leaf'], [['leaf', 'leaf']]]]], [['leaf', 'leaf'], ['leaf', 'leaf'], [[[[['leaf', 'leaf', 'leaf'], ['leaf'], ['leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf', 'leaf']]], ['leaf', 'leaf']], [['leaf', 'leaf', 'leaf'], [['leaf'], [['leaf'], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf']], []], [[['leaf'], [['leaf']], ['leaf', 'leaf', 'leaf']], [[], [['leaf', 'leaf', 'leaf'], [[[['leaf', 'leaf', 'leaf'], [[[['leaf'], [], ['leaf', 'leaf'], ['leaf']], ['leaf'], [], [['leaf', 'leaf'], ['leaf'], [['leaf', 'leaf', 'leaf'], ['leaf', 'leaf'], [], ['leaf', 'leaf', 'leaf']], [['leaf'], ['leaf', 'leaf', 'leaf']]]], ['leaf']], [['leaf', 'leaf', 'leaf'], [], ['leaf', 'leaf'], []], ['leaf', 'leaf', 'leaf']], [[[[[['leaf', 'leaf']], [[['leaf', 'leaf'], ['leaf'], ['leaf', 'leaf']], [[[['leaf', 'leaf', 'leaf']], ['leaf']]], [[['leaf'], ['leaf'], [['leaf', 'leaf']]]]], ['leaf', 'leaf']]]]], [['leaf', 'leaf'], ['leaf', 'leaf'], [[['leaf'], [['leaf', 'leaf'], [[[['leaf', 'leaf'], [['leaf'], [], [[], ['leaf'], ['leaf', 'leaf']]], [['leaf', 'leaf', 'leaf'], ['leaf']]], ['leaf', 'leaf', 'leaf'], []], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf']]], [['leaf', 'leaf', 'leaf']], []]]]]], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf', 'leaf'], [['leaf']]], ['leaf', 'leaf', 'leaf']]], [['leaf'], [], [['leaf'], ['leaf', 'leaf', 'leaf'], ['leaf'], [['leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']]]], ['leaf', 'leaf'], []]], ['leaf']]
# >>> tree_generator()
# [['leaf'], ['leaf', 'leaf'], ['leaf', 'leaf']]

