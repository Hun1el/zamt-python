from math import *
def a(n, x):
    mem = (n**(1/n))/cos(n * x)
    return mem
def b(n, x):
    sum = 0
    for i in range(1, n + 1):
        mem = a(i, x)
        sum += mem
        print(mem, f"Сумма: {sum}")
    return sum
n= int(input("Введите n: "))
x = float(input("Введите x: "))
result = b(n, x)
print(f"Итоговая сумма: {result}")