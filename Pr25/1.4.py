class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cauisine_type = type
    number_served = 0
    def describe_restaurant(self):
        print ("Название ресторона:" + self.restaurant_name)
        print ("Тип ресторона:" + self.cauisine_type)
    def open_restaurant(self):
        print ("Ресторан" + " " + self.restaurant_name + " " + "открыт")
    def set_number_served(self, n):
        self.number_served = n
    def increment_number_served(self, n):
        self.number_served += n
        print(self.number_served)
        
obj1 = Restaurant("Мур-Мур", "9")
obj1.describe_restaurant()
obj1.open_restaurant()
obj1.set_number_served(1)
obj1.increment_number_served(400)