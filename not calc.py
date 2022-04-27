def nani(input_arg):
    def nani2(func):
        def wrapper(*args, **kwargs):
            z = []
            for i in args:
                if i is None:
                    z.append(0)
                else:
                    z.append(i)
            return func(*z, **kwargs)

        return wrapper

    return nani2


@nani(2)
def main(x, y):
    sum = lambda x, y: x + y
    notsum = lambda x, y: x - y
    um = lambda x, y: x * y
    delen = lambda x, y: x // y
    return sum(x, y), notsum(x, y), um(x, y), delen(x, y)


print(main(None, 2))
