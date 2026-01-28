from lessons.lessons_2.python_2 import number_1

a = 10
b = 20.5


a += 5
add_A = a + 5
print(add_A)
print(a)

#операції порівняння

#==
print(100 == 100)

#!= не дорівнюе
print(20 != 40)

# >= більше або дорівнюе
# <= меньше або дорівнюе
print(10 >= 10)
print(10 <= 10)

num_1 = 6
number_2 = 5
nam_name = "orange"
print("Number: ", num_1  != number_2)
print("type: ", type(num_1) == type(number_2))
print("Id: ", id(num_1) == id(number_2))

print("orange: ", num_1 == len(nam_name))

bool_1 = True
bool_2 = False

if (num_1 == number_2) == bool_1:
    print(True)

#догічні операції
x = 10
y = 20
print(x>8 and y > 10 and x ==y) #якщо все вірно

sasha_age = 14
eva_age = 13
if sasha_age > 13 and eva_age >= 13 and sasha_age != eva_age:
    print("both 13 years")

male_age = 22
is_maried = True
city = "Lviv"
if male_age > 18 and is_maried == True and city == "Lviv":
    print("cool")

else:
    print("Its not cool")

#or - або (якщо хоч одна умова вірна то буде True)
if sasha_age > 13 or eva_age > 10:
    print("both 13 years")

#not - не (міняє занчення на протилежне)

if not sasha_age > 18:
    print(Not )