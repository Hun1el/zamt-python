class User:
    def __init__ (self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    login_attempts = 0
    def describe_user(self):
        print("Имя: " + self.first_name)
        print("Фамилия: " + self.last_name)
        print("Возраст: " + self.age)
        print("Место жительства: " + self.location)
    def great_user(self):
        print("Здравствуйте, " + self.first_name + " " + self.last_name + "!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print (self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
obj1 = User("Максимус", "Сидоркин", "20", "Городец")
obj1.increment_login_attempts()
print(obj1.login_attempts)
obj1.reset_login_attempts()
print(obj1.login_attempts)