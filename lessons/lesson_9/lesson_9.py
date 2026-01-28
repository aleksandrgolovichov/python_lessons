print("Hello from terminal")

list_1 = ["one", "two", "sun"]
# set_1 = {"two"}
# dict_1 = {"two": 1}
# tuple_1 = {"two",}

if "sun" in list_1:
    print(list_1.index("sun"))
    if len(list_1) >= 3:
        print("add 1 more")
        list_1.append("moon")
        print(list_1)
    if len(list_1) > 3:
        print("more then 3")
    else:
        print("less more 3")
else:
    print("No sun")
    for i in list_1:
        print(i)

a = 25
b = 45




# if умова:
#   Блок коду
# у іншому випадку:
#    блок коду
# translate = input("Enter your language (ua/en): ")
#
# if translate == "сонце":
#         print("translate: Sun")
# elif translate == "кіт":
#         print("translate: Cat")
# elif translate == "машина":
#         print("translate: Car")
# else:
#         print("No translate")
#
#
# print("End")
