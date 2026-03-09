from math import *
n = int(input("Введите число строк квадратной матрицы:\n"))
B = []
for i in range(n):
    B.append([])
    for j in range(n):
        ctan = tan(i)
        if ctan == 0:
            ctan = 1
        B[i].append(1/pow(ctan, 2)-sqrt(3*j+2))
print("Сгенерированная матрица: ")
for row in B:
    print(row)
min3 = B[2][0]
for i in B:
    min3 = min(i[2], min3)
print("Минимальный элемент третьей строки: ", min3)
sum_column = 0
for i in range(n):
    sum_column += B[i][1]
print("Сумма элементов второго столбца матрицы: ", sum_column)
negative_element = 1
for i in range(n):
    for j in range(n):
        if B[i][j]<0:
            negative_element *= B[i][j]
print("Произведение отрицательных элементов матрицы: ", negative_element)           
outfile = open("lab13_1.out", "w")
outfile.write("Сгенерированная матрица:\n")
for i in range(n):
    for j in range(n):
        outfile.write(str(B[i][j]) + " ")
    outfile.write("\n")
outfile.write(f"Минимальный элемент третьей столбца: {min3}\n")
outfile.write(f"Сумма элементов второго столбца: {sum_column}\n")
outfile.write(f"Произведение отрицательных элементов: {negative_element}\n")
outfile.close()