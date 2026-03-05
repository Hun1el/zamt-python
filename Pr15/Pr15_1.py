with open('lab_15_1.txt', 'r') as file:
    x = int(file.readline())
    y = int(file.readline())
result = (x > 15 and y <= 20) or (x == 15 or y == 20)
with open('lab_15_1_out.txt', 'w') as file:
    file.write(str(result))
print(result)