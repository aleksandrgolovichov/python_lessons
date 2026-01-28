my_set = set()
print(type(my_set))
print(dir(my_set))

my_set2 = {1,2,3,3,4,5,6,7,8,9,0, True,False,"hello"}
print(my_set2)
print(type(my_set2))
print(len(my_set2))

my_set2.add = "new element"
print(my_set2)
my_set2.remove("3")

