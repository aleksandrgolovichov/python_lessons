from collections.abc import async_generator

from control_robot.CR import my_dict

my_list = ["Hello", True, 1.11, 52]
print(type(my_list))
print(id(my_list))
print(len(my_list))
print(my_list[1:3])
my_list[1] = False
my_list[1:3] = ["Python"]
my_list.insert(1, "new item")
print(my_list)
my_list.append("last item")
print(my_list)
my_list.extend({"dog": 1909, "cat": 2020})
print(my_list)
my_list.remove(52)
print(my_list)
my_list.pop(5)
print(my_list)
del my_list[0]
print(my_list)
# my_list.clear()
# print(my_list)
for x in my_list:
    print(x.upper())
print("*"*100)

for i in range(10):
    print(i)
for i in range(len(my_list)):
    print(f"index: {i}, value: {my_list[i]}")

my_fruits = ["apple", "banana", "cherry", "melon"]
my_fruits.sort()
print(my_fruits)
new_list = []

for fruits in my_fruits:
    if "a" in fruits:
        new_list.append(fruits)
        print(fruits)

print(new_list)

my_list2 = [fruits.capitalize() for fruits in my_fruits if "a" in fruits]
print(my_list2)



my_dict = {"Best_Friend": "Vova",
           "age": 15,
           "city": "Kyiv",
           "school": "Gymnasium №236",
            "hobby": ("scateboarding", "walking in the park"),
           "favorite_color": ("Red","White"),}

print(my_dict)
print(f"My best friend is", my_dict['Best_Friend'],", he living in", my_dict['city'])



my_dict["country"] = "Ukraine"
print(my_dict)

del my_dict["school"]
print(my_dict)

for x in my_dict:
    print(x,':', my_dict[x])

my_friends = {
    "first_friend":{"Name": "Vova",
                    "age": 15,
                    "country": "Ukraine"},
    "second_friend":{"Name": "Lera",
                     "age": 15,
                     "country": "Cyprus"},
    "third_friend":{"Name": "Artem",
                     "age": 15,
                     "country": "Germania"}

}

print(my_friends)
