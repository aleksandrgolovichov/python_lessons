# str_1 = "Hello"
# str_2 = "World"
# print(str_1+ "" + str_2)
# print(str_1 * 10)
# print(str_1[0])
# print(str_2[-1])
# print(id(str_1))
# str_1 = "h" # This will raise a TypeError because strings are immutable in Python
# str_1 += "everyone"
# str_1 = str_1 + " everyone"
# print(id(str_1))
#
# some_list = [1, 2, 3]
# print(id(some_list))
# some_list.append("New Element")
# print(some_list)
# print(id(some_list))
# print(id(some_list[3]))
# print(id(some_list)) == id(some_list)
#
#
# print(str_1.count("o"))
# print(str_1.find("o"))
# print(str_1.index("o"))
# print(f"Immutable: {str_1.upper()}")
# print("Immutable: {},{}".format(str_2, "Python"))
# print("Immutable: (item_2},{item_1}".format(item_1=str_2, item_2="Python"))
#
# int_var = 42
# float_var = 3.14
# bool_var = True
#
# print(str(int_var)*10)
# print(int(bool_var))
# list_1 = ["berlin1991",3.14, True, [1,2,3, ["a", "b", "c"]]]
# print(list_1[-1][-1])
# list_1.append("new line")
# print(list_1)
# list_1.remove(3.14)
# del_first_el = list_1.pop(0)
# print(del_first_el)
# print(list_1)
#
#
# dict_1 = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
#
# dict_1[4] = "four"
# print(dict_1)
# del dict_1[2]
# print(dict_1.get(3))
#
# tuple_1 = (1, 2, 3, "four", [5,6,7])
# print(tuple [1][4][0])
# set_1 = {1, 2, 3, 4, 4, 4, 5}
# print(set_1)
# set_1.add(6)
# print(set_1)
# set_1.remove(3)
# print(set_1)
# set_1.add("three")
# set_1.add("1three")
# print(set_1)
# set_2 = {1, 2, 3, 10}
# print(set_1 | set_2)
# print(set_1 & set_2)

list_3 = []

# for i in range(20):
#     if i % 2 == 0:
#         list_3.append(i)

for i in range(0,20,2):
    if i >= 10:
        list_3.append(i)

print(list_3)

list_4 = [i for i in range(0,20,2) if i < 10]
print(list_4)

for i in range(0):
            print(1)
else:
            print(2)


# x = [1,2,3]
# print(''.join(x))

*r, = range(3)
print(r)


lst = [1, 2, 3]
print(lst.pop(1))

print(~False)

x = [0.1] * 10
print(sum(x))

a = {'a': 10, 'b': 20}
b = {'b': 25, 'c': 30}
print(a | b)

x = [[1]] * 3
x[1][0] = 0
print(x[0][0])
# [1], [1], [1]]

a = 1
b = 2.0
print(sum(a,b))