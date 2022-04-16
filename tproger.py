def f(a):
    new_f = []
    for i in a:
        if i <= 5:
            new_f.append(i)
    return new_f


def f2(arr1, arr2):
    array = []
    for num in arr1:
        if num in arr2:
            array.append(num)
    return array



