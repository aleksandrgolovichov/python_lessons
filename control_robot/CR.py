

x_int = 10
y_float = 3.14
z_complex = 2 + 3j

print(type(x_int), abs(x_int), pow(x_int, 2))
print(type(y_float), round(y_float), int(y_float))
print(type(z_complex), z_complex.real, z_complex.imag)

TF = True
print(type(TF), int(TF))

text = "Hello, Python!"
print(type(text), text.upper(), text.lower(), text.replace("Hello", "Hi"))

my_list = [1, 2, 3, "a", False,True]
print(type(my_list), len(my_list))
my_list.append(100)
del my_list[True]
my_list.pop(1)
print(my_list)

my_tuple = (10,10,10, 20, 30)
print(type(my_tuple), my_tuple.count(30), my_tuple.index(20))
print(my_tuple)


my_set = {1, 2, 2, 3}
print(type(my_set), my_set.union({4, 5}))


my_dict = {"a": 1, "b": 2}
print(type(my_dict), my_dict.keys(), my_dict.values(), my_dict.get("a"))

