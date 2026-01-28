def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a or b == 0:
        return "Error: division by zero"
    return a / b


print("Choose an operation: \n 1-Add \n 2-Minus \n 3-Multiply \n 4-Divide")


choice = int(input("Choose an operation (1-4): "))

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

while True:
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", minus(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")
    break
