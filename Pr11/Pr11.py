#Задание 1
file = open("learning_python.txt", "r")
content = file.read()
print("Чтение файла:")
print(content)
file.seek(0)
print("\nПеребор строк файла:")
for line in file:
        print(line.strip())
file.seek(0)
lines = file.readlines()
print("\nwith блок:")
print(lines)
file.close()
#Задание 2
file = open("learning_python.txt", "r")
for message in file:
        message = message.replace("Python", "JavaScript")
        print(message)
file.close()
#Задание 3
y_name = input("Введите ваше имя: ")
file = open("guest.txt", "w")
file.write(y_name)
print(f"Ваше имя {y_name}, сохранено в файле!")
file.close()
#Задание 4
file = open("guest_book.txt", "a")
while True:
        name = input("Введите имя: ")
        if name.lower() == "q":         #Выход из цикла на q
                break
        print(f"Привет, {name}!")
        file.write(f"{name}\n")
file.close()
#Задание 5
file = open("10.5.txt", "a")
while True:
        a = input("Причина: ")
        if a.lower() == "q":            #Выход из цикла на q
                break
        file.write(f"{a}\n")
print("Спасибо за ответ!")
file.close()