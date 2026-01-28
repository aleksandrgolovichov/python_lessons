# def muntiply():
#     """"This function returns the product of 5 and 4."""
#
#     return 5 * 4
# print(())
#
# def count(a=1, *args, **kwargs):
#     num_of_args = len(args)
#     return a + num_of_args
# print(count(10, 2, 3, 4, 5))


def Grietting(name1,name2, Grit="Hello"):
    """Ми пишемо F строку для вітання двох нами заданих імен."""
    return f"{name1} say {Grit} {name2}!"
print(Grietting(name1="Joel", name2="Maria"))
print(Grietting.__doc__)


def mu_funk():
    print("hello world")
    return sum([10, 20, 30, 40, 50])

#mu_funk()
numb_sum = mu_funk()
print(type(numb_sum))
print(type(mu_funk()))

print("#"*100)

def my_func2 (name):
    print(name + "Hello world!")
    return name
my_func2("John")
my_func2("Alice")
my_func2("Bob")


def my_func3 (*fruits):
    print("fruits received:", fruits)
    print("second item", fruits[1])

my_func3("apple", "banana", "cherry")


print("#"*100)
def my_func4 (**person):
    print("person received:", person)
    print("name:", person.get("name"))
    print("age:", person.get("age"))

my_func4(name="John", age=30, city="New York")


def avg2(a, b):
    result = a + b
    return result / 2
print(avg2(10, 20))

def sum4(a, b, c, d):
    result = a + b + c + d
    return result
print(sum4(1, 2, 3, 4))

def avg4(a, b, c, d):
    result = a + b + c + d
    return result / 4
print(avg4(4, 8, 12, 16))


def mult3(a, b, c):
    result = a * b * c
    return result
print(mult3(2, 3, 4))

def sub3(a, b, c):
    result = a - b - c
    return result
print(sub3(20, 5, 3))

def avg_sum_mult(a, b):
    result = (a + b) + (a * b)
    return result / 2
print(avg_sum_mult(3, 5))

def second_item(*data):
    print("all data:", data)
    print("second item:", data[1])
second_item("red", "gray", "blue")


def square_avg(a, b):
    result = (a + b) / 2
    return result * result
print(square_avg(4, 6))

def count_items(*args):
    print("items:", args)
    print("count:", len(args))
count_items("a", "b", "c", "d")


def my_funk3(a, b, c):
    result = a + b + c
    return result / 3
print(my_funk3(20, 812, 39))


# 18.01.26

car_list = ["Toyota","Nissan","Mazda","Tesla","Mercedes","BMW","Audi"]
Name_list = ["Sasha","Valeria","Vova","Jamal","Vlad","Olga","Igor"]
# print(len(car_list))
# def car_funk(cars):
#     for car in cars:
#         print(car)
# car_funk(car_list)
#
# def name_funk(names):
#     for name in names:
#         print(name)
# name_funk(Name_list)



# for car in car_list:
#     print(car)


# def owners_cars(cars, names):
#     # print(f"this people owners car:{names}")
#     # print(f"all cars:{cars}")
#     for car in cars:
#         print(car)
#     for name in names:
#         print(name)
#     print(f"This people{name} have this car:{car}")
#
# owners_cars(cars=car_list, names=Name_list)

def owners_cars(cars, names):
    car_owner = {

    }
    # for key in names:
    #     for value in cars:
    #         # print(value)
    #         car_owner[key] = value
    print(car_owner)
    # car_owner["Sasha"] = cars[0]
    # car_owner["Valeria"] = cars[1]
    # car_owner["Vova"] = cars[2]
    # car_owner["Jamal"] = cars[3]
    # car_owner["Vlad"] = cars[4]

    # for value in car_owner.values():
    #      print(value)
    #     car_owner[key] = cars[3]
    #     print(car_owner)
    #     # print(f"Owner:{key}, Car:{value}")
    #     for i in range(len(names)):
    #         car_owner[key] = cars[i]
    # # print(car_owner)
    # for values in cars:

    for i in range(len(names)):
         car_owner[names[i]] = cars[i]
    print(car_owner)
    for key,value in car_owner.items():
        print(key, value)
    return len(car_owner)
print(owners_cars(cars=car_list, names=Name_list))

def dell(a,d):
    return a-d
print(dell(10,44))

