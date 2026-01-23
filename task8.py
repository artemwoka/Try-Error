"""
Помилки (номери рядків через пробіл, цей рядок - №2):
"""


# Наведено список ПІБ. Знайдіть найпоширеніше по-батькові.
# Якщо немає по-батькові, людина не враховується в розрахунку.
try:
    n = int(input("Введіть кількість людей: "))
except ValueError:
    print("Помилка: введено некоректне значення. Будь ласка, введіть число.")
    n = 0
    

middle_names = {}
count = 0
for i in range(n):
    fio = input("Введіть ПІБ через пробіл: ").split()
    
    try:
        middle_name = fio[2]
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        count += 1
    except IndexError:
        continue
if middle_names:
    most_common = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
    print("Найпоширеніше по-батькові:", most_common)
else:
    print("Немає по-батькові для розрахунку.")

print("Людей брало участь у розрахунку:", n)