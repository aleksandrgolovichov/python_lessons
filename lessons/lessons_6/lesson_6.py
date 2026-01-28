name = "sasha"
age = 14
height = 1.80
surname = "Holovichov"

# int(), float(), str(), bool() - функції перетворення типів даних
#bool(15) - true
#bool(0) - false
#bool("") - folse
#bool("Hello") - true
#len('name') / 4 - довжина рядка
#id(name) # - функція для визначення уникального індефікатора обʼєкта в памʼяті
#list_exemple = [1,2,,3,4,5] # - список
list_exemple = [1,2,3,4,5]
print(type(list_exemple))
list_1 = [10, name, age, height, True,"Hello"]
print(len(list_1))
print(list_1[0]) # - звернення до елемента списку
list_sasha = list(name)
print(list_sasha)
print(id(list_1[1]))
print(id(list_1[0]))
print(id(list_1[-1]))
print(id(list_1[::-1]))
list_1.reverse()
print(list_1)
teacher = "Viktoria"
list_1.append(teacher) # - додавання елемента в кинець списку
print(list_1)
list_1.insert(2, "python") # - додавання елемента в певну позицію
list_1.pop(1)
list_1.remove("Viktoria")

list_2 = [1,2,3,4,3,2,1]
list_2.sort()
print(list_2)
list_1.clear()
print(list_1)

list_2[0] = "two"
print(list_2)

list_3 = ["sasha", age, height, True, "Open-Wrld" ]

print(f"my first {list_3[0]} and last {list_3[1]}")
list_3.remove(True)
list_3.insert(3, "python")
list_3.append("FootBall")
print(list_3)
