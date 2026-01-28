#while True:
# print("This will run forever.")
# break
# counter = 0
# while counter < 5:
#     print("Counter is:", counter)
#     counter += 1
#     counter = counter + 1
#     while True:
#         value = input("Type 'exit' to break the loop: ")
#         if value == 'exit':
#             print("Exiting the loop.")
#             break
#     print("exited the inner loop")


fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    fruits.append("orange")
    print(fruits)
    break

some_list = [1, 2, 3, 4, True, "hello", 5.6]
for item in some_list:
    print(item)
    if isinstance(item, str):
        print("found a string:", item)
        break

word = "hello"
for letter in word:
    print(letter)

print(range(5))

print(range(10))
list_nambers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_nambers2 = list(range (1000, 2000, 100))
print(list_nambers)
print(list_nambers2)

for number in list_nambers:
    print(number**2)

#HW


colors_list = ["red", "green", "blue",38, 28.3, False]

i = 2

while i < len(colors_list):
    item = colors_list[i]
    print(item)
    if isinstance(item, str):
        print("found a string:", item)
        break
    i += 1


def owners_cars(cars, names):
    car_owner = {

    }
    for values in cars:
            for kay
    for i in range(len(names)):
        print(i)
        for car in cars:
            print(car, names[i])


owners_cars(cars=car_list, names=Name_list)

