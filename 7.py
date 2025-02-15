def power(x, y=2):
    """Повернути x^y."""
    if y == 0:
        return 1
    elif y < 0:
        raise ValueError(f"У значення не може бути від'ємним ({y})")
    else:
        return x * power(x, y - 1)

try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as exc:
    print("Помилка:", exc, "Перевірте початкові дані")
except Exception as exc:
    print("Помилка:", exc)
