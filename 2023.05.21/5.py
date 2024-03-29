def logger(function: 'callable') -> 'callable':

    """Функция декоратор, который в стандартном потоке вывода ведёт журнал вызовов декорируемой функции"""
      
    def wrapper(*args, **kwargs) -> 'any':
        
        # СДЕЛАТЬ: лучше перечислить сначала все позиционные аргументы с их значениями по умолчанию, а затем все ключевые с их значениями по умолчанию

        arguments = [f'{arg}' for arg in args] + [f'{k}={v}' for k, v in kwargs.items()]

        if function.__defaults__ is not None:
            for def_arg in function.__defaults__:
                if function.__code__.co_argcount != len(args):
                    arguments += [f'{def_arg}']                    
               
        if function.__kwdefaults__ is not None:
            for k, v in function.__kwdefaults__.items():
                if k not in kwargs:
                    arguments += [f'{k}={v}']

        print(f'{function.__name__}({", ".join(arguments)}) -> ', end='')
            
        try: 
            print(result := function(*args, **kwargs))
            return result
        except Exception as exception:
            print(f'\n\t{type(exception).__name__}:', str(exception))
        
    return wrapper


# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) ->  0.33
# 0.33
# >>>
# >>> div_round(10, 2)
# div_round(10, 2, digits=0) ->  5.0
# 5.0
# >>> div_round(5, 0)
# div_round(5, 0, digits=0) ->
        # ZeroDivisionError: division by zero
# >>>




# >>> def div_round1(num1, num2=2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round1 = logger(div_round1)
# >>> div_round1(25, digits =2)
# КОММЕНТАРИЙ: не самый лучше способ расположения аргументов
# div_round1(25, digits=2, 2) -> 12.5
# 12.5
# >>> div_round1(25, 3)
# div_round1(25, 3, digits=0) -> 8.0
# 8.0
# >>>
# >>> div_round1(11)
# div_round1(11, 2, digits=0) -> 6.0
# 6.0
# >>> div_round1(11,0)
# div_round1(11, 0, digits=0) ->
        # ZeroDivisionError: division by zero
# >>>


# >>> def div_round3(num1, num2=2):
# ...     return num1 / num2
# ...
# >>> div_round3 = logger(div_round3)
# >>> div_round3(25, 5)
# div_round3(25, 5) -> 5.0
# 5.0
# >>>
# >>> div_round3(33)
# div_round3(33, 2) -> 16.5
# 16.5
# >>>
# >>> div_round3(33,0)
# div_round3(33, 0) ->
        # ZeroDivisionError: division by zero
# >>>


# >>> def div_4(num1,num2):
# ...     return num1 / num2
# ...
# >>> div_4 = logger(div_4)
# >>> div_round3(100,50)
# div_round3(100, 50) -> 2.0
# 2.0
# >>>


# КОММЕНТАРИЙ: порадовали большим количество тестов! загвоздка в том, что в этой задаче их требуется ещё больше...)

# СДЕЛАТЬ: изучите пример, запустите предложенные тестовые функции со своей реализацией декоратора, найдите недочёты


# ИТОГ: хорошо, но можно лучше — 4/7
