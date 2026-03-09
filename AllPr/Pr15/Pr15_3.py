import array as a
from math import *
mass1=a.array('f',range(0))
for i in range (1,11):
    print(f'Введите {i}-й элемент массива')
    mass1.append(float(input()))
b=float(input('Введите число b: '))
mass2=a.array('f',range(0))
for i in range (len(mass1)):
    a=sqrt(mass1[i]+b)**3-tan(mass1[i])**2
    mass2.append(a)
print(mass2)
minB=min(mass2)
print(f'Минимальный элемент массива B: {minB}')
mass2[mass2.index(min(mass2))],mass2[9]=mass2[9],mass2[mass2.index(min(mass2))]
print(mass2)