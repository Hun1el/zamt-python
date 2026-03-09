import os
print("Текущая папка:", os.getcwd())
print("Файлы здесь:", os.listdir("."))

from math import *
x = float(input("Введите x: "))
y = float(input("Введите y: "))
if x < 2 and y > 4:
    f = cos(x) ** 2 + y
elif 2 < x <= 3 or y < 4:
    f = (4 - x) / (abs(y) + 1) - 3
else:
    f = x * y
with open('lab_15_2_out.txt', 'w') as file:
    file.write(f"{f}")
print(f)