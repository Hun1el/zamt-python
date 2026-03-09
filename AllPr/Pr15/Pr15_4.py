C = []
for i in range(8):
    a = int(input("Введите элемент для массива C: "))
    C.append(a)
D = []
for i in range(6):
    a = int(input("Введите элемент для массива D: "))
    D.append(a)
del C[2]
D.append(77)
D.insert(3, 44)
CD1 = C + D
CD1.sort()
CD2 = []
for i in range(1, len(CD1), 2):
    CD2.append(CD1[i])
CD2 = CD2[-2:] + CD2[:-2]
print("Массив C после удаления третьего элемента:", C)
print("Массив D после добавления 77 и 44:", D)
print("Массив CD1 после сортировки:", CD1)
print("Массив CD2 после сдвига элементов на 2 вправо:", CD2)
with open("lab_15_4_out.txt", "w") as file:
    file.write("Массив C после удаления третьего элемента: " + str(C) + "\n")
    file.write("Массив D после добавления 77 и вставки 44: " + str(D) + "\n")
    file.write("Объединенный массив CD1 после сортировки: " + str(CD1) + "\n")
    file.write("Массив CD2 после сдвига элементов на 2 вправо: " + str(CD2) + "\n")
