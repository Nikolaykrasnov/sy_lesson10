pets = {}

name = input("Введите имя питомца: ")

pets[name] = {}
pets[name]["Вид питомца"] = input("Введите вид питомца: ")
pets[name]["Возраст питомца"] = int(input("Введите возраст питомца: "))  
pets[name]["Имя владельца"] = input("Введите имя владельца: ")

age = pets[name]["Возраст питомца"]
if age % 10 == 1:
    print(f"Его возраст: {age} год")
elif 1 < age % 10 < 5: 
    print(f"Его возраст: {age} года")
else:
    print(f"Его возраст: {age} лет")
    
print(f"Это {pets[name]['Вид питомца'].lower()} по кличке \"{name}\". {pets[name]['Имя владельца']}")
