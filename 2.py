"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def primes(a, b):
    """Повернути список простих чисел на відрізку від 'a' до 'b'."""
    res = []
    for i in range(a, b + 1):
        c = 0
        for j in range(i):
            if i % (j + 1) == 0:
                c += 1
            if c == 2:
                res.append(i)

    return res