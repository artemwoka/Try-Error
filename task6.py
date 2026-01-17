"""
Помилки (номери рядків через пробіл, цей рядок - №2): 11 14 15
"""


def unemployment_rate(unemployed, employed):
    """Повернути рівень безробіття (РБ) як частку від 1.

       Розрахунок за формулою: РБ = безробітні / (зайняті + безробітні).
    """
    if employed + unemployed == 0:
        raise ZeroDivisionError("Сума зайнятих і безробітних не може бути нулем.")
    else:
        return unemployed / (unemployed + employed)

try:
    unemployed = int(input("Введіть кількість безробітних (людей): "))
    employed = int(input("Введіть кількість зайнятих (людей): "))
    rate = unemployment_rate(unemployed, employed)
    print(f"Рівень безробіття = {rate:.1%}")
except ValueError:
    print("Помилка: введено некоректне значення. Будь ласка, введіть число.")
except ZeroDivisionError as zde:
    print(f"Помилка: {zde}")
except Exception as e:
    print(f"Сталася помилка: {e}")
