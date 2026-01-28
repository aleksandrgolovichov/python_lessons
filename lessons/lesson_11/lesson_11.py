a = range(100)
#print(list(a))
number = 1
while number <= 5:
    print(f"Number = (number)")
    number += 1
    print("Inside loop")
print("End of loop")

massege = "Hello, World!"
for char in massege:
    print(char)
for i in range(10):
    print(i, end = "1")

for i in range(10):
    print(i * "*")




i = 1
k = 1

while i < 10:
    print(k * i, end = " ")
    k += 1
    print("/n")
    k += 1
    i += 1
    break

print("*" * 20)

list_items = [1,1.1,"hello", True, 5, 6.7, "world", False]

for item in range(len(list_items)):
    print(list_items[item], item)


list_name = ["Anna", "Bob", "Charlie", "Diana"]
list_ages = [25, 30, 22, 28]
for i in range(len(list_name)):
    print(f"{list_name[i]} is {list_ages[i]} years old.")
print("*"* 120)
for name, age in zip(list_name, list_ages):
    print(f" {name} is {age} years old.")


list_2 = []
for i in range(10):
    list_2.append(i * 2)
print(list_2)


list_3 = []
for i in range(10):
    list_3.append(i)
print(list_3)

