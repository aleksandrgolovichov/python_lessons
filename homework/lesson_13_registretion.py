users = {}

while True:
    print("1 - Реєстрація")
    print("2 - Вхід")
    print("3 - Змінити пароль")
    print("4 - Видалити акаунт")
    print("5 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        username = input("Введіть логін: ")
        if username in users:
            print("Такий користувач уже існує!\n")
        else:
            password = input("Введіть пароль: ")
            users[username] = password
            print("Реєстрація успішна!\n")

    elif choice == "2":
        username = input("Логін: ")
        password = input("Пароль: ")
        if username in users and users[username] == password:
            print(f"Вітаємо, {username}! Ви увійшли в акаунт.\n")
        else:
            print("Невірний логін або пароль!\n")

    elif choice == "3":
        username = input("Логін: ")
        old_pass = input("Поточний пароль: ")
        if username in users and users[username] == old_pass:
            new_pass = input("Новий пароль: ")
            users[username] = new_pass
            print("Пароль змінено!\n")
        else:
            print("Невірні дані!\n")

    elif choice == "4":
        username = input("Логін: ")
        password = input("Пароль: ")
        if username in users and users[username] == password:
            del users[username]
            print("Акаунт видалено!\n")
        else:
            print("Невірний логін або пароль!\n")

    elif choice == "5":
        print("До побачення!")
        break

    else:   
        print("Невірний вибір!\n")