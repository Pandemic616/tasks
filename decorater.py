def decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('stop')
        return func

    return wrapper


#
# @decorator
# def decor_func(x):
#     print(x * 2)
#
# decor_func(18)

import time


def benchmark(func):
    import time
    def wrapper(arg1, arg2):
        start_time = time.time()
        ret_val = func(arg1, arg2)
        end_time = time.time()
        print(f"Time = {end_time - start_time}")
        return ret_val

    return wrapper


# @benchmark
# def add(x, y):
#   return x + y
# print(add(4, 4))


def numer2(func):
    def wrapper(*args, **kwargs):
        if any(list(map(lambda x: x == 2, args + tuple(kwargs.items())))):
            print(2)
        else:
            print(False)
        return func(*args, **kwargs)

    return wrapper


#
#
# @numer2
# def add(x, y):
#     return x + y
#
#
# print(add(2, 4))


def errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            return f'произошла ошибка {err}'

    return wrapper


# @errors
# def add(x, y):
#     return x // y
# print(add(2, 0))

def pod(input_arg):
    def pod2(func):
        def wrapper(*args, **kwargs):
            return f'{input_arg}'

        return wrapper

    return pod2


@pod(10)
def add(x, y):
    return x + y


print(add(2, 2))
