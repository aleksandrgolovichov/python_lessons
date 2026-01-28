# Filter-фільтруе послідовність, залишаючи лише ті елементи, для яких функція повертає True.

# def evem_numbers(num):
#     return num % 2 == 0:
#         return True
#     return False
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers_list = list(filter(evem_numbers, numbers))
# print(even_numbers_list)

def even_number(number):
    if number % 2 == 0:
        return True
    return False

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(even_number, numbers))
# print(even_numbers)


some_numbers = [11, 22, 33, 44, 55, 66, 77]
new_list = []
for i in some_numbers:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)

even_numbers_lambda = list(filter(even_number, some_numbers))
print(even_numbers_lambda)