    """
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def f(x):
    """Повернути значення функції.

    Функція не обробляє винятки.
    """
    return x**2 / (x + 2) - 3


k = int(input("Введіть межу інтервалу [-k; k]: "))
h = float(input("Введіть крок: "))

x = -k
print("x".rjust(10), "f(x)".rjust(10))
while x <= k:
    # Якщо помилка виникає під час обчислення функції,
    # Необхідно вивести тире "-"
    # Цей випадок повинен обробити другий вкладений блок try
    print(f"{x:10.2f} {f(x):10.2f}")

    x += h