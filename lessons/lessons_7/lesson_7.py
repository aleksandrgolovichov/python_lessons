name_info = ["mark, bob, vesta"]
list_info_str = ''.join(name_info)
print(list_info_str)



name = input("Enter your name: ")
age = int(input("Enter your age: "))
owner_car = input("Enter your car owner (Type car-brand): ")

list_info = [name, age, owner_car]
print(list_info)

second_car = input("Enter your second car owner (Type car-brand): ")
list_info.append(second_car)
print(f"I have a car: {list_info[2] and  list_info[3]}")

money = int(input("Enter your money:"))
if money >= 100000:
    print("You can buy a new car")
    new_car = input("Enter your new car (Type car-brand): ")
    list_info.append(new_car)
else:
    print("you need  more money")
    sell_car = input("Enter your sale car Brand: ")
    sell_car_price = int(input("Price sell_car: "))
    list_info.remove(sell_car)
    all_money = money + sell_car_price
    list_info.append(all_money)

print(list_info)

print(f"Your name is (list_info[0].upper()), you are (list_info[1]} years old, you have a car: {list_info [2]} and {list_info[3]}, now you have {list_info[4]} money.")

