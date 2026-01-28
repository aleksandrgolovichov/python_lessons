from lessons.lessons_7.lesson_7 import name_info

my_string = "Hello, World!"
print(len(my_string))# Output: 13
print(my_string.upper())# Output: W
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title())
print(my_string.strip())# Output: "Hello, World!
print(my_string.rstrip())
print(my_string.lstrip())
print(my_string.find("word"))# Output: 7
my_string2 = "hello, python, word, spase!"
print(my_string2.split(", "))# Output: ['hello', ' python', ' word', ' spase!']
print(my_string2.count("hello"))# Output: 1
my_string3 = ['Hello', 'Python!, World2, Space', 'Hello','HELLO']
result_str3 = ",".join(my_string3)
print(result_str3)
print("/".join(my_string))
print('lorem ipsum dolor sit amet')
print("lorem ipsum dolor sit amet")
print("""lorem ipsum dolor sit amet""")

name = "John"
last_name = "Doe"
age = 30

fool_name = name + " " + last_name
print(fool_name)

introduction = f"My name is {name} {last_name} and I am {age} years old."

introduction2 = "My name is %s and I am %d years old.".format(name, last_name, age)

introduction3 = "My name is {0} {1} and I am {2} years old.".format(name, last_name, age)

my_string4 = "This is a simple string for testing.\n \t this string contains multiple words."
print(my_string4)

if "World" in my_string and "Hello" in my_string:
    print("Found 'World' in the string!")
else:
    print("Not found in the string.")

some_string = "The quick brown"
print(some_string.find("quick"))
print(some_string[14:19])
