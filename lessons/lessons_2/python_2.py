print("hello")

name = "sasha"
age = 14
surname = "Holovichov"

print("My name is", name, "i'm", age, "years old", "surname is", surname)
print(name + str(age) + surname)
print(f"My name is {name} , {age}, {surname}")

print("Type Int - ціле число - intager - 1 2 10 100 1000")

x = 10
y = 20
print(x+y)
print(y-x)
print(x / y)
print(y * x)
print(x ** 2)
print(x / 4)
print(y // 3) #//-ділення націло
print(y % 3) # %-залішок від ділення

number_1 = y / 2
print(str(number_1))
print(int(number_1))
print(str(int(number_1)))
print(type(number_1))

print("Type float - число з крапкою - float - 1.1 2.2 1.10 1.100 1.1000")
x = 10.6
y = 20.2
print(x+y)
print(y-x)
print(x / y)
print(y * x)
print(x ** 2)
print(x / 4)
print(y // 3)
print(y % 3)

import math
print(math.pi)
print(math.e)
print(math.sqrt(81))

katet_1 = 5
katet_2 = 8
gipot = math.hypot(katet_1, katet_2)
print(round(gipot, 3))