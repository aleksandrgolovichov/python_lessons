
# while True:
#     user_input = input("Введіть число: ")
#
#     try:
#         number = int(user_input)
#         print("Квадрат числа:", number ** 2)
#         break
#     except ValueError:
#         print("Помилка! Введене значення не є числом. Спробуйте ще раз.")


# user_input = input("Введіть число: ")
#
# try:
#     result = "Результат: " + user_input + 0.1
#     print(result)
#
# except TypeError:
#     print("Помилка: не можна додавати рядок та число без перетворення типів.")
#
#     try:
#         number = int(user_input)
#         print("Результат:", number + 0.1)
#     except ValueError:
#         print("Ви ввели не число. Перетворення неможливе.")
