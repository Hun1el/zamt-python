def make_car(manufacturer, model, **other_car_info):
    car = {"manufacturer":manufacturer,"model":model}
    car.update(other_car_info)
    return car
car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

def make_car(manufacturer, model, **other_car_info):
    car = {"manufacturer": manufacturer, "model": model}
    car.update(other_car_info)
    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
