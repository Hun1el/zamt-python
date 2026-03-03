# Задание 1
from math import *

x = float(input("Введите x: "))
s = float(input("Введите значение s: "))

if x**2 - x <= 1:
    f = x**3 - 3 * x + 8 * sin(s)
else:
    f = 1 / (x**3 - 3 * x + s**2)
print("x=", x, "s=", s, "f=", f, sep=" ")
# Задание 2
import math

k1 = float(input("Введите k1: "))
k2 = float(input("Введите k2: "))
a_start = -1
a_end = 6
delta_a = 0.3

for a in range(int(a_start * 10), int(a_end * 10) + 1, int(delta_a * 10)):
    a /= 10.0
    argument = abs(1 / (math.tan(a) ** 2) - k1)

    if k2 - a == 0:
        print(f"При a = {a}, знаменатель (k2 - a) равен нулю, деление на ноль")
    else:
        result = math.log(argument) / (k2 - a)
        print(f"При a = {a}, z(a) = {result}")

# Задание 3
import math

k1 = float(input("Введите k1: "))
k2 = float(input("Введите k2: "))
a = -1.0
delta_a = 0.3

print("{:<10} {:<10}".format("x =", "z(a) ="))

while a <= 6.0:
    z = (math.log(abs(1 / math.tan(a**2))) - k1) / (k2 - a)

    print("{:<10.2f} {:<10.4f}".format(a, z))

    a += delta_a

# Задание 4
from math import *

k1 = float(input("Введите k1: "))
k2 = float(input("Введите k2: "))
a = -1.0
delta_a = 0.3

while True:
    if a <= 6:
        z_a = abs((1 / (tan(a**2) - k1))) / (k2 - a)

        print("При a = {:.2f}, z(a) = {:.4f}".format(a, z_a))

        a += delta_a
    else:
        break

print("Программа завершена")
