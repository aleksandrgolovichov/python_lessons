integer = "2"
print(str(integer))
print(type(integer))

first = "Hello"
second = "World"

print(first + "," + second + "!")

pravda = True
rist = 1.88

my_list = [integer, first, pravda, rist,second]
for item in my_list:
    print(f"Значення: {item}, Тип: {type(item)}")


dictionary = {
    "integer": 2,
    "string": "Hello, World!",
    "float": 1.88,
    "boolean": True,
    "list": [1, 2, 3]
    }
print("*"*100)
for i in my_list:
    print(i)
    dictionary[str(i)] = i
# dictionary["pravda"] =  my_list[2]
# dictionary["integer"] = my_list[1]
# dictionary["rist"] = my_list[3]

print(dictionary)
cortage = (42, "Python", 2.718, False, [4, 5, 6], {"key": "value"})
for item in cortage:
    print(f"Значення: {item}, Тип: {type(item)}")
print(*cortage)


while True:
    num_str = input("Введіть число або 0 для закінчення операції: ")
    num = int(num_str)
    if num == 0:
        break
