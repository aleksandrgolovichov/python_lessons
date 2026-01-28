while True:
    try:
        first_num = int(input("Введіть перше число: "))
        second_num = int(input("Введіть друге число: "))
    except ValueError:
         print("Write correct number, not string/text!")
    operation = input("Введіть операцію (+, -, *, /): ")


    if operation == "+":
        result = first_num+second_num
        print(result)

    elif operation == "-":
        result = first_num-second_num
        print(result)

    elif operation == "*":
        result = first_num*second_num
        print(result)

    elif operation == "/":
        try:
            result = first_num / second_num
            print(result)
        except ZeroDivisionError:
            print("Ділення на нуль неможливе!")
    else:
        print("Невідома операція, спобуйте ще раз.")
        break
