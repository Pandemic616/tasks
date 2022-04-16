def f(a):
    new_f = []
    for i in a:
        if i <= 5:
            new_f.append(i)
    return new_f


def f2(s, d):
    g = []
    for i in s:
        if i in d:
            g.append(i)
    return g


print(f2([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
