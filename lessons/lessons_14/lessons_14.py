#try, except, else ta finally.
#num_1 = 10
#num_2 = input("Введіть число: ")
# print(num_1/num_2)
# try:
#result = num 1/ num 2
#   print("Результат ділення:", result)
# except TypeError:
#   print("Ділення на нуль неможливе!")
#
# try:
#     res = 2/0
# except ZeroDivisionError:
#     res = 2/int(input("Введіть число відмінне від нуля: "))
#     print(res)
#
# try:
#     res = 2/0
# except ZeroDivisionError:
#     res = 2/int(input("Введіть число відмінне від нуля: "))
#     print(res)
#
# try:
#     a = input("Введіть число - 1: ")
#     b = input("Введіть число - 2: ")
#     print(int(a)/int(b))
# except  ZeroDivisionError:
#     print("Ділення на нуль неможливе!")
# except (ValueError, TypeError, ZeroDivisionError):
#     print("Ввести тільки числа!")
# else:
#     result = c**2
#     print("Результат:", result)
# finally:
#     print("Операція завершена.")



# while True:
#     a = input("Введіть число 1: ")
#     b = input("Введіть число 2: ")
#     try:
#         c=int(a) / int(b)
# except (ValueError):
#     print("Введені некоректні дані. Спробуйте ще раз.")
# except ZeroDivisionError:
#     print("Ділення на нуль неможливе. Спробуйте ще раз.")
# else:
#     print("Результат ділення:", с)
#     break

# while True:
#     a = input("Введіть число 1: ")
#     b = input("Введіть число 2: ")
#     if a.isdigit() and b.isdigit():
#         print("Числа:", a,b)
#         if int(b) == 0:
#             print("Результат ділення на нуль неможливий!")
#         else:
#             c=int(a)/int(b)
#             print("Результат ділення:", c)
#         break
#     else:
#         print("NOT NUMBERS!", a,b )



frouts = {
    "banana": 12,
    "chery": 20,
    "apple": 22,
}
print(frouts)
print(frouts["banana"])
# print(frouts["kiwi"])

try:
    print(frouts["apple"])
except KeyError:
    frouts["kiwi"] = 32
    print("Kiwi added to froots dict")
else:
    print("Kiwi not in froots dict")
finally:
    print("All froots:", frouts)

print("hello")











