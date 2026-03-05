from math import *
def a(message):
    print(f"Ошибка: {message}")
def b(x, k1):
    if x < -1 or x > 3:
        a("Значение x должно быть [-1, 3]")
        return 
    if x == 0:
        a("(ctg(|x|) = 0, при x = 0)")
        return 
    result = (pow(cos(3*x), 2)*k) / (3*k*1/tan(abs(x)))
    return result
x = float(input("Введите значение x: "))
k = float(input("Введите значение k: "))
result = b(x, k)
if result:
    print(f"Значение функции при x={x}, k={k}, Результат: {result}")