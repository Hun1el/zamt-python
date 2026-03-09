from math import pi, atan, inf
def compute_population(t):
    try:
        year_people = (C/r)*((pi/2)-atan((T-t)/r))
    except:
        year_people = inf
    return year_people
C = 172
T =  2000
r = 45
line = input("Список лет через пробел: ")
years_list = [int(x) for x in line.split()]
pop_list = []
for year in years_list:
    pop_list.append(compute_population(year))
for i in range(len(years_list)):
    print("%5d - %6.3f миллиард(ов)"% (years_list[i],pop_list[i]))