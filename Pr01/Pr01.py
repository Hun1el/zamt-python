result1 = 2 + 5
print("Пример 1: ", result1)

result2 = 3 * (5 - 8)
print("Пример 2: ", result2)

result3 = 2.4 + 3.0 / 2
print("Пример 3: ", result3)

tseloe = 10
drobnoe = 8.4
stroka = "No"

big_netseloe = tseloe * 3.5

drobnoe -= 1

print("Результат деления tseloe на drobnoe: ", tseloe / drobnoe)
print("Результат деления big_netseloe на drobnoe: ", big_netseloe / drobnoe)

stroka = stroka + "No" + "_" + "Yes" * 3

print("tseloe =", tseloe)
print("drobnoe =", drobnoe)
print("stroka =", stroka)
print("big_netseloe =", big_netseloe)

name = input("What is your name? ")

age = input("How old are you? ")

location = input("Where are you live? ")

print("This is", name)
print("It is", age)
print("He live in", location)

num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

sum_result = num1 + num2
diff_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
floor_div_result = num1 // num2
mod_result = num1 % num2

print("Сумма: ", sum_result)
print("Разность: ", diff_result)
print("Умножение: ", mul_result)
print("Деление: ", div_result)
print("Целочисленное деление: ", floor_div_result)
print("Остаток от деления: ", mod_result)
