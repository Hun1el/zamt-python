def build_profile(first_name, last_name, **other_info):
    profile = {"first_name":first_name, "last_name":last_name}
    profile.update(other_info)
    return profile
my_profile = build_profile("Барышев", "Иван", age = 17, location = "Смирино", group = "ИС-22А")
print("Профиль:")
for key, value in my_profile.items():
    print(f"{key}:{value}")

def build_profile(first_name, last_name, **other_info):
    profile = {"first_name": first_name, "last_name": last_name}
    profile.update(other_info)
    return profile

my_profile = build_profile("Барышев", "Иван", age=17, location="Смирино", group="ИС-22А")
print("Профиль:")

for key, value in my_profile.items():
    print(f"{key}: {value}")