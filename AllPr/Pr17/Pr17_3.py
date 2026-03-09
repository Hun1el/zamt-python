from math import *
def input_array():
    return [float(input(f"Введите элем. массива D[{i}]: ")) for i in range(15)]
def V(array, b):
    return [(b**2 * cos(sqrt(abs(x)) + 1))/(b + 0.3) for x in array]
def replace_m(array):
    min_value = min(array)
    array[0] = min_value
    return array
def count_m(array):
    min_value = min(array)
    return array.count(min_value)
def print_array(array):
    print("Массив: ", array)
D = input_array()
b = float(input("Введите b: "))
result = V(D, b)
print_array(result)
result = replace_m(result)
print_array(result)
mcount = count_m(result)
print(f"{mcount}")