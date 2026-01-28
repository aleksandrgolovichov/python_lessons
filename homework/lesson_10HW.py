
print("1. Створіть множину із списку")
transport_list = ['boat', 'bus', 'plane', 'train']
transport_set = set(transport_list)
print("Множина:", transport_set)
print("-" * 40)


print("2. Перевірка числа на парність")
number = int(input("Введіть ціле число: "))
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
print("-" * 40)


print("3. Непарні числа від 1 до 25:")
odd_numbers = list(range(1, 26, 2))
print(odd_numbers)
print("-" * 40)

("4. Цикл while з break:")
counter = 0
while True:
    print("Лічильник:", counter)
    counter += 1
    if counter == 5:
        print("Зупинка циклу на числі 5")
        break
print("-" * 40)


print("5. Вивід чисел від 3 до 60:")
numbers = list(range(3, 61))
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
print("-" * 40)



print("6. Цикл for з if, else і while:")
for i in range(1, 8):
    if i % 2 == 0:
        print(f"{i} — парне число")
        j = 0
        while j < 2:
            print("Це вкладений цикл while")
            j += 1
    else:
        print(f"{i} — непарне число")
print("-" * 40)
