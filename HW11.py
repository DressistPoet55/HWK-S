# Task 1 Положительные аргументы функции
def validate_arguments(func):
    def wrapper(*args):
        for i in args:
            if i <= 0:
                raise ValueError("Неверный аргумент")
        return func(*args)
    return wrapper


@validate_arguments
def my_function(x, y):
    return f'x: {x}, y: {y}'


print(my_function(1, 2))


# Task 2 Вернуть число
def chislo_ilinet(func):
    def wrapper(*args):
        reslt = func(*args)
        if reslt is not isinstance(int, float):
            print('Результат не является числом')
        return reslt
    return wrapper


@chislo_ilinet
def test_chislo(bukva):
    return bukva


print(test_chislo("a"))


# Task 3 Декоратор типов
def typed(types):
    def dec(func):
        def wrapper(*args):
            chngd_args = [types(arg) for arg in args]
            return func(*chngd_args)
        return wrapper
    return dec


@typed(types=str)
def add(a, b):
    return a + b


print(add("3", 5))
print(add(5, 5))
print(add('a', 'b'))


@typed(types=int)
def add1(a, b, c):
    return a + b + c


print(add1(5, 6, 7))


@typed(types=float)
def add2(a, b, c):
    return a + b + c


print(add2(0.1, 0.2, 0.4))


# Task 4 Функция кэширования *
def cache(func):
    def wrapper(*args):
        d = {}
        if args in d:
            return d
        else:
            result = func(*args)
            d = result
            return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
