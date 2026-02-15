# from curses import wrapper
#
#
# def uppercase_name(name):
#     def wrap(*args, **kwargs):
#         result = name(*args, **kwargs)
#         return result.upper()
#     return wrap
#
# @uppercase_name
# def greet(name):
#     return f"Hello, {name}!"
#
# greeting = greet("World")
# print(greeting)
#
#
#
# def sum_dec(funk):
#     def wrap(*args, **kwargs):
#         result = funk(*args, **kwargs)
#         result_list2 = []
#         for i in result:
#             result_list2.append(i**2)
#         return sum(result_list2)
#     return wrap
#
# @sum_dec
# def some_values():
#     return list(range(5))
#
# print(some_values("world"))
#
# @sum_dec
# def numbers_for_sum():
#     some_numbers = []
#     for i in range(1, 40,2):
#         some_numbers.append(i)
#     return  some_numbers
#
# print(numbers_for_sum())
#
#
# def my_decorator(func):
#     def wrapper():
#         print("Before the function call.")
#         result = say()
#         print(result)
#         print("After the function call.")
#
#
# def say_hello():
#     print("Hello, World!")
#     return "Greeting has been printed."
# say_hello()



def my_decorator(say):
    def wrapper():
        print("Before the function is called.")
        result = say()
        res_list = result.split()
        res_list.reverse()
        print(res_list)
        print("After the function is called.")
    return wrapper

@my_decorator
def some_text():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
some_text()

@my_decorator
def say_hello():
    print("Hello, World!")
    return "Greeting has been printed."
say_hello()


def show_decorator(func):
    def wrupper(*args, **kwargs):
        print(type(args[1]))
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrupper

@show_decorator
def add(a, b,c,**kwargs):
    return a+b+c

def add (a,b):
    return a + b

print(add(1,2))