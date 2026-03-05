from math import *
m = int(input("Введите количество членов ряда:\n"))
x = float(input("Введите x:\n"))
summ = 0
with open("lab14.out", "w") as file:
    for n in range(1, m + 1):
        a = sin(x - n) / n * (n ** 2 + 5)
        print(a)
        file.write(f"Слагаемое {n}: {a}\n")
        summ += a
    print(f"Итоговая сумма {summ}")
    file.write(f"Итоговая сумма: {summ}\n")