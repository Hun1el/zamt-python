def count(str):
    a = "aeiouAEIOU"
    b = 0
    for i in str:
        if i in a:
            b += 1
    return b
string = "Hi"
result = count(string)
print("Кол-во гласных букв в строке:", result)
