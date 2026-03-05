def message(name):
    print(f"Привет, {name}! Добро пожаловать!")
def calc(a, b):
    return a + b
name = input("Введите ваше имя: ")
message(name)
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result = calc(num1, num2)
print(f"Сумма чисел {num1} и {num2} равна {result}")