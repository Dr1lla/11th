"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def power(x, y=2):
    """Повернути x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


x = int(input("x="))
y = int(input("y="))
print(power(x, y))