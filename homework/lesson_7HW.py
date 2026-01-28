a = 10
b = 5.7
c = "Hello"
my_list = [a, b, c, False]
second_element = my_list[1]
print("Другий елемент списку: ", second_element)

months = {
"January": 1,"February": 2,"March": 3,"April": 4,"May": 5
}

months["June"] = 6
del months["January"]
del months["March"]
months["April"] = 8
months["May"] = 9

print("Оновлений словник:", months)

print(type(months))
print(months.keys())
print(months.values())
