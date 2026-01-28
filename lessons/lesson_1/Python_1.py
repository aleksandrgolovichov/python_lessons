x=4
y=1

if x == y:
  print("число равное")

else:
  print("число не равное")  


print(id(x))
print(id(y))
print(x)

'''
  olux
  diki
'''
print("Sasha","Golovichov","Alekseevich")
print(20 * ("ovechka "))
name = input("введите ваше имя: ")
if name == "Sasha":
    print("Привет,Саша!")

else:
    print("Привет незнакомец!")

# Типи даних: 
# str-строка, текст - "Hello"
# int-чілі числа 
# float-числа з крапкою
# bool- логічні типи даннях (true\false)

my_integer = 42
print("Тип my_integer:", type(my_integer))

my_float = 3.14
print("Тип my_float:", type(my_float))

print("Адреса my_integer в пам'яті:", id(my_integer))
print("Адреса my_float в пам'яті:", id(my_float))


reserved_words = ["if", "else", "while", "for", "def", "return", "class"]
print("Зарезервовані слова Python:", reserved_words)