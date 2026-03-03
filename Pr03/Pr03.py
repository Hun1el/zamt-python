# Задание 1
login = "Max"
password = "123456!"

login_input = input("Введите логин:")
password_input = input("Введите пароль:")

if login_input == login and password_input == password:
    print("Доступ разрешён. Привет, " + login + "!")

elif login_input != login and password_input != password:
    print("Доступ запрещён - логин и пароль неверные!")

elif login_input != login:
    print("Неверный логин!")

else:
    print("Неверный пароль!")
# Задание 2
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
oper = input("Введите знак операции:")

if oper == "+":
    result = number1 + number2
    print("Сумма: " + str(result))
elif oper == "-":
    result = number1 - number2
    print("Вычитание: " + str(result))
elif oper == "/":
    result = number1 / number2
    print("Деление: " + str(result))
elif oper == "*":
    result = number1 * number2
    print("Умножение: " + str(result))
elif oper == "//":
    result = number1 // number2
    print("Целочисленное деление: " + str(result))
elif oper == "%":
    result = number1 % number2
    print("Остаток от целочисленного деления: " + str(result))
else:
    print("Ошибка - неверный знак операции!")
# Задание 3
x = 5
y = 10
exp1 = x < y and y > 0
exp2 = x == 5 and y != 5
exp3 = x > y and y < 0
exp4 = x != 5 and y == 5

orexp1 = x < y or y > 0
orexp2 = x == 5 or y != 5
orexp3 = x > y or y < 0
orexp4 = x != 5 or y == 5

string1 = "Hello"
string2 = "world"

exp5 = string1 == "Hello" and string2 == "world"
exp6 = string1 == "goodbye" or string2 == "world"
exp7 = string1 == "hi" and string2 == "there"
exp8 = string1 != "Hello" or string2 != "world"


print("Ответ первого лог. выражения: ", exp1)
print("Ответ второго лог. выражения: ", exp2)
print("Ответ третьего лог. выражения: ", exp3)
print("Ответ четвёртого лог. выражения: ", exp4)

print("Ответ первого лог. выражения: ", exp5)
print("Ответ второго лог. выражения: ", exp6)
print("Ответ третьего лог. выражения: ", exp7)
print("Ответ четвёртого лог. выражения: ", exp8)

print("Ответ первого лог. выражения: ", orexp1)
print("Ответ второго лог. выражения: ", orexp2)
print("Ответ третьегоо лог. выражения: ", orexp3)
print("Ответ четвёртого лог. выражения: ", orexp4)
# Задание 4
value = int(input("Введите значение value: "))

if value > 0:
    print("Значение переменной больше 0")
elif value < 0:
    print("Значение переменной меньше 0")

if value > 0:
    print(1)
elif value < 0:
    print(-1)
else:
    print("Значение переменной равно 0")
# Задание 5
secret_num = 10

user_num = int(input("Попробуйте угадать число: "))

if user_num == secret_num:
    print("Поздравляю, вы угадали число!")
elif user_num < secret_num:
    print("Введенное число меньше загаданного!")
else:
    print("Введенное число больше загаданного!")
