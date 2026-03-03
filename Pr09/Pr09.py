#Задание 1
menu = ("Салат", "Суп", "Мясо", "Рыба", "Потато")

print("Меню ресторана:")
for i in menu:
    print(i)

new_menu = ("Томато", "Суп с мясом", "Мясо с рыбой", "Морепродукты", "Томато")

print("\nОбновленное меню ресторана:")
for i in new_menu:
    print(i)
#Задание 2
technical_school = {
    "ИС-23А": 25,
    "ИС-23Б": 25,
    "ИС-22А": 25,
    "ИС-22Б": 25,
    "ИС-21А": 25,
    "ИС-21Б": 25
}
students_in_group = technical_school["ИС-22А"]
print(f"В группе ИС-22А {students_in_group} студентов.")
technical_school["ИС-22А"] = 0 # изменение на 3 курсе
technical_school["ИС-24А"] = 25
technical_school["ИС-24Б"] = 25
del technical_school["ИС-22Б"]
print("\nОбновленное содержимое:", technical_school)
#Задание 3
cities = {
    "Москва": {
        "country": "Россия",
        "population": "более 12 миллионов",
        "fact": "Москва - Самый крупный город страны."
    },
    "Париж": {
        "country": "Франция",
        "population": "около 2 миллионов",
        "fact": "Париж - город любви и искусства."
    },
    "Нью-Йорк": {
        "country": "США",
        "population": "более 8.5 миллионов",
        "fact": "Нью-Йорк - город, известный своими небоскребами."
    }
}
for city, info in cities.items():
    print(f"Город: {city}")
    print(f"Страна: {info['country']}")
    print(f"Население: {info['population']}")
    print(f"Интересный факт: {info['fact']}")
#Задание 4
num = {1, 2, 3, 4, 5, 6}
result = sum(i ** 2 for i in num)
print("\nСумма квадратов 6-ти элементов: ", result)
#Задание 5
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
for fruit in sorted(fruits, reverse=1):
    print(fruit)
