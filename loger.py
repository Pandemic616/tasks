# значит есть функция которой на вход идут данные  x, y
# функция делит эти числа
# функция вызывается несколько раз( один раз идет вызов с параметрами 1, 0)
# нужен декоратор который в случае ошибки будет ее обрабатывать и записывать в файл эту ошибку
# фаил должен быть один, должен пополнятся


def log_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                bag_file = open("Log_ERROR.txt", "a", encoding="UTF-8")
                bag_file.write(f'произошла ошибка {err}\n')
                bag_file.close()
                return f'произошла ошибка {err}'

        return wrapper










@log_error
def division(x, y):
    return x//y


division(1, 1)
division(1, 2)
division(1, 0)
