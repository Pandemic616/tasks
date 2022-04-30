"""
начит есть функция которой на вход идут данные  x, y
функция делит эти числа
функция вызывается несколько раз( один раз идет вызов с параметрами 1, 0)
нужен декоратор который в случае ошибки будет ее обрабатывать и записывать в файл эту ошибку
фаил должен быть один, должен пополнятся
"""
from functools import wraps
from typing import Callable


def log_error(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable | str:
        try:
            return func(*args, **kwargs)
        except Exception as err:
            bag_file = open("Log_ERROR.txt", "a", encoding="UTF-8")
            bag_file.write(f'произошла ошибка {err}\n')
            bag_file.close()
            return (
                f'произошла ошибка {err}: '
                f'funcname={func.__name__}, '
                f'funcmodule={func.__module__}, '
                f'funcdoc={func.__doc__}'
            )

    return wrapper


@log_error
def division(x: int, y: int) -> float:
    """Производит деление чисел"""
    return x / y


division(1, 1)
division(1, 2)
division(1, 0)
