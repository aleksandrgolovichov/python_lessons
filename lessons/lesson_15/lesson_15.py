# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[1])
#
# try:
#     print(list[11])
# except IndexError:
#     print("Індекс виходить за межі списку")
# finally:
#     print("Завершення обробки індексу")
from operator import truediv

item_str = "Hello"
if item_str == "hello":
    print("You entered Hello")
else:
    print("You did not enter Hello")

print(item_str.upper())
item_int = 3
print(item_int**2)
print(str(item_int)+"Hello")

item_float = 2.9
print(item_float-3.9)
print(bool(item_float))

item_bool = False
if item_bool is True:
    print("Item is true")
else:
    print("Item is False")
print(int(item_bool))

item_list = [1, 2, 3]
print(item_list[0])
print(item_list[::2])
if 2 in item_list:
    print("there is 2")
else:
    print("there is no 2")
item_dict = {
    "one": 1,
    "two": 2
}
print(item_dict.keys())
print("one" in item_dict)
if "three" not in item_dict:
    print("there is no three")
else:
    print("there is three")



item_set = {1, 2, 3, 4}
# print(item_set[2])
item_set.pop()
item_set.add(5)
print(item_set)

for i in item_set:
    print(i**2)

item_frozenset = (["a", "b", "c"])
while True:
    for d in item_frozenset:
        print("Found d in frozenset")

    else:
        item_frozenset.append("d")
        break

item_tuple = (1,2,3)
print(len(item_tuple))
print(item_tuple[1:2])
for i in item_tuple:
    print((i/2)**2)


print("*"*120)

for i in item_tuple:
    print(i*item_int)
print(item_int*item_tuple[2])
print(item_set.add(item_int))