import math
def f_x(x):
    try:
        y = 1/(x+3)+2*x+3
    except:
        y = math.inf
    return y
a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))
if n <= 0 or a >= b:
    print("Ошибка!")
else:
    h = (b - a)/(n - 1)
    x_l = [a + i * h * h for i in range(n)]
    f_l = [f_x(x) for x in x_l]
    
    print("-" * 17)
    print("| %4s | %6s |" % ("x", "f(x)"))
    print("-" * 17)
    for i in range(n):
        print("| %4.1f | %6.3f |" % (x_l[i], f_l[i]))
    print("-" * 17)