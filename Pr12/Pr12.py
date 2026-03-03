file = open("data_A.txt", "r")
dataA = file.readline()
F = dataA.split("\t")
F = list(map(int, F))
file.close()

from math import *
k = int(input("Введите число k:\n"))
G = []
for i in range(len(F)):
    if F[i] >= 0:
        G.append((k**3)+(k*sin(F[i]))/(pow(F[i], 1/2)+1))
    else:
        G.append((k**3)+(k*sin(F[i]))/(-pow(fabs(F[i]), 1/2)+1))
for i in range(len(G)):
    print("{0:.2f}" .format(G[i]), end = " ")
summ = 0
for num in G:
    if num < 0:
        summ += num
print("\nСумма отриц. :", round(summ, 2))
for i in range(len(G)):    
    if i % 2 == 0:
        G[i] = fabs(summ)
for i in range(len(G)):
    print("{0:.2f}" .format(G[i]), end = " ")
with open('data_B.txt','a') as out:
    print(round(summ,2), file = out)
    print(G, file = out)
