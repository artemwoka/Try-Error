"""
Помилки (номери рядків через пробіл, цей рядок - №2): 11 14 15
"""


def power(x, y=2):
    """Повернути x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except RecursionError:
    print("Помилка: досягнуто максимальну глибину рекурсії.")
except ValueError:
    print("Помилка: введено некоректне значення. Будь ласка, введіть число.")
except Exception as e:
    print(f"Сталася помилка: {e}")