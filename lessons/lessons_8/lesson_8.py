


my_tuple = ("apple", "banana", "cherry", 44, True)
print(my_tuple.__dir__())
print(type(my_tuple))

print(my_tuple[-1])
print(my_tuple[1])
print(my_tuple[1:2])
print(my_tuple.count("apple"))
print(my_tuple.index("cherry"))
print(len(my_tuple))
a,b,c,d,i = my_tuple
print(a,b,c,d,i)

list_my_tuple = list(my_tuple)
print(list_my_tuple)
list_my_tuple.append("new element")
my_tuple = tuple(list_my_tuple)