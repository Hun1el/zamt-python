class User:
    def __init__ (self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print("Имя: " + self.first_name)
        print("Фамилия: " + self.last_name)
        print("Возраст: " + self.age)
        print("Место жительства: " + self.location)
    def great_user(self):
        print("Здравствуйте, " + self.first_name + " " + self.last_name + "!")
obj1 = User("Максимус", "Сидоркин", "20", "Городец")
obj2 = User("Кобан", "Бршев", "60", "Смирино")
obj1.describe_user()
obj1.great_user()
obj2.describe_user()
obj2.great_user()