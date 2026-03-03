# Задание 1
input_str = input("Введите строку (не менее 20 символов): ")

if len(input_str) < 20:
    print("Ошибка! Строка должна содержать не менее 20 символов.")
else:
    mod_str = input_str[0].upper() + input_str[1:].lower()
    mod_str = mod_str.replace("a", "o")  # Ввод на должен быть на англ.
    mod_str = mod_str.ljust(45)

    print("Измененная строка: ", mod_str)

# Задание 2
input_str = input("Введите строку (не менее 20 символов): ")

if len(input_str) < 20:
    print("Ошибка: введенная строка слишком короткая.")
else:
    mod_str = ""

    for a in input_str:
        if a != " ":
            mod_str += a * 2
        else:
            mod_str += a

    print("Изменённая строка: ", mod_str)
# Задание 3
input_str = input("Введите строку (не менее 20 символов), содержащую буквы и цифры: ")

if len(input_str) < 20:
    print("Ошибка: введенная строка меньше 20 символов.")
else:
    c_c = 0  # Cчетчик согласных
    c = set("bcdfghjklmnpqrstvwxyz")

    for a in input_str:
        if a.isalpha() and a.lower() in c:
            c_c += 1

    print("Кол-во согл. лат. букв в введенной строке:", c_c)
