# 1. Створити об’єкт типу str та задати йому змінну
my_str = "Rainbow"
# 1.1 Вивести на екран його тип
print(type(my_str))

# 2. Створити ціле число та задати йому змінну g
g = 25
# 2.1 Вивести на екран тип g
print(type(g))

# 2.3 Перетворити тип змінної g в строку та присвоїти змінну g_string
g_string = str(g)
# 2.4 Вивести на екран тип g_string
print(type(g_string))

# 3. Задати text = ‘Hello’. Розмножити ‘Hello’ 10 раз
text = "Hello"
print(text * 10)

# 4. Написати декілька речень з використанням символа \n
print("Python is fun!\nIt is easy to learn.\nLet's code together!")

# 5. Задати змінну letters, яка містить алфавіт
letters = "abcdefghijklmnopqrstuvwxyz"
print("Перша буква:", letters[0])
print("Остання буква:", letters[-1])



# 1. Створити пустий список зі змінною list1
list1 = []

# 2. Створити список list2, який буде містити три пори року
list2 = ["winter", "spring", "summer"]

# 2.1 Добавити в список list2 autumn
list2.append("autumn")

# 2.2 Дістати зі списку list2 spring
print(list2[1])  # spring

# 3. Створити список list3, який буде містити цифри від 1 до 5
list3 = [1, 2, 3, 4, 5]

# 4. Створити список all_list та помістити туди списки list1,list2,list3
all_list = [list1, list2, list3]
print(all_list)

# 5. В list2 замінити перший елемент [1] на summer
list2[1] = "summer"
print(list2)
