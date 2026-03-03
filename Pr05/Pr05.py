# Задание 1
corr_num = 4 * 100 - 54

user_num = int(input("Решите пример: 4 * 100 - 54 = "))

if user_num == corr_num:
    print("Поздравляем! Вы правильно решили пример.")
else:
    print("Ошибка. Правильный ответ:", corr_num)
# Задание 2
print("Четные числа от 0 до 20:")
for i in range(0, 21, 2):
    print(i, end=" ")

exit

print("\nКаждое третье число от -1 до -21:")
for i in range(-1, -22, -3):
    print(i, end=" ")

# Задание 3
secret_num = 7
attempts = 0

while True:
    ent_num = int(input("\nВведите число: "))
    attempts += 1

    if ent_num == secret_num:
        print(f"Поздравляем! Вы угадали число {secret_num} с {attempts} попытки.")
        break
    else:
        print("Попробуйте ещё раз!")
# Задание 4
kilometers_1_day = 2
total_kilometers = 0

for day in range(1, 15):
    total_kilometers += kilometers_1_day
    kilometers_1_day += 0.5

print(f"Суммарное расстояние: {total_kilometers} километров")
