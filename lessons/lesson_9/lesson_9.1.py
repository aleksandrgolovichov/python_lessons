print("Calculator")

# while True:
#
# try:
#     num1 = float(input("Enter first number: "))
#
#
#     print("Choose operation: ")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#     operation = input("Enter operation (+, -, *, /): ")
#
#     num2 = float(input("Enter second number: "))
#
#     if operation == "1" or operation == "+":
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#
#     if operation == "2" or operation == "-":
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#
#     if operation == "3" or operation == "*":
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
#
#     if operation == "4" or operation == "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"{num1} / {num2} = {result}")
#         else:
#
#             print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Invalid input. Please enter numeric values.")

num1 = 10
num2 = 20
num3 = 30

if num1 and num2 > num3:
    print("num1 or num2 is greater than num3")

else:
    print("num3 is the greatest")


if num3 or num2 > num1:
    print("num3 or num2 is greater than num1")

else:
    print("num1 is the greatest")

if not num1 >num2:
    print("num1 is not greater than num2")

else:
    print("num1 is greater than num2")