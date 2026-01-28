# [Вираз for item in теребельний_обект if умова]
number_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
number_s = []
for i in number_list:
    number_s.append(1*10)
print(number_s)




# number_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
number_s = [i*10 for i in number_list  if i %20 == 0]
print(type(number_list), number_s)


list_1 = [i**2 for i in range(0,20,2)] # list comprehension
print(list_1)

list_1 = []
for i in range(0, 20, 2):
    list_1.append(i ** 2)

print(list_1)


list_1 = {i:str(i**2)for i in range(0,20,2)} # dict comprehension
print(list_1)

list_2 = []
for num in range(10):
    if num % 2 == 1:
        list_2.append(num**2)
    else:
        list_2.append((num**4))
print(list_2)

list_2_conmprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]

dict_2_conmprehension = {num: str(num * 2) if num % 2==1 else num * 4 for num in range(10)}
print(dict_2_conmprehension)