class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cauisine_type = type
    def describe_restaurant(self):
        print ("Название ресторона:" + self.restaurant_name)
        print ("Тип ресторона:" + self.cauisine_type)
    def open_restaurant(self):
        print ("Ресторан" + " " + self.restaurant_name + " " + "открыт")
obj1 = Restaurant("Мур-Мур", "9")
obj1.describe_restaurant()
obj1.open_restaurant()