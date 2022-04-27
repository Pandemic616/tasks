from functools import cache


num = int(input())


def fibonachi(n):
    if n <= 1:
        return 0
    else:
        x, y = 0, 1
        print(x)
        for i in range(n - 1):
            x, y = y, x + y
            print(x)


fibonachi(num)
# @cache
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(500))