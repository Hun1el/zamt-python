# Задание 1
age = int(input("Введите ваш возраст: "))

if age < 18:
    print("Вы несовершеннолетний")
else:
    if age < 65:
        print("Вы взрослый")
    else:
        print("Вы пенсионер")

print("Программа завершена")
# Задание 2
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 > num2:
    num3 = num1 - num2
elif num1 < num2:
    num3 = num1 + num2
elif num1 == num2:
    num3 = num1
else:
    num3 = num1 * num2
print("Значение третьей переменной: ", num3)
# Задание 3
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

if x > 0 and y < 2:
    f = 5 + x - y
elif x < 0 or 2 <= y < 12:
    f = 4 - x * y
else:
    f = y + x

print("Значение f = ", f)
# Задание 4
day = int(input("Введите номер дня недели (от 1 до 7): "))

if day >= 1 and day <= 7:
    if day == 1:
        print("Понедельник")
    elif day == 2:
        print("Вторник")
    elif day == 3:
        print("Среда")
    elif day == 4:
        print("Четверг")
    elif day == 5:
        print("Пятница")
    elif day == 6:
        print("Суббота")
    elif day == 7:
        print("Воскресенье")
else:
    print("Некорректный ввод. Номер дня недели должен быть от 1 до 7.")
