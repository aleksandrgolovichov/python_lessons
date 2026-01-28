
login = []
password = []
print(login, password)
while True:
    user_login = (input('Enter your login: '))
    user_password = int(input('Enter your password: '))
    login.append(user_login)
    password.append(user_password)

    print("enter your account")
    print(login, password)

    exist_login = input('Enter your login: ')
    exist_password = int(input('Enter your password: '))

    if exist_login in login and exist_password in password:
        print('You are logged in')
    else:
        print('Invalid login or password')

    break