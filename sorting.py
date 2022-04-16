# сортировка массива
import random

array = [5, 5, 2, 3, 4, 2, 1, 6]


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)


print(QuickSort(array))
