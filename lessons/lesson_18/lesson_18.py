# function

def greet(name):
    return f"hello, {name}!"


print(greet("World"))


def add():
    return 24 + 54


print(sum([1, 2, 3, 4, 5]))

def add(a):
    print("Start function")
    s = a**2
    print(s)
    return s

print(add(51))
print(add(6))

print(add(13))

d = 25 + add(7) + sum ([10, 20, 30])
print(d)


print(add.__doc__)
print("#" * 80)
print(sum.__doc__)




def add(width, height):
    return width**2,height ** 2

s = add(3, 5)
print("Площа Прямокутника:", s)


def add(a,d,f):
    return a+d+f
triangle_s = add(10,12.5,15)
print("Площа трикутника",triangle_s)





def func_2(arg_2, arg_1=5, arg_3="Hello", arg_4=None):
    list_funk_2 = [arg_1, arg_2, arg_3, arg_4]
    for i in list_funk_2:
        print(f"type of {i}: {type(i)} and id of {i}: {id(i)}")
    if arg_1 == 5:
        return "Enter a difference value"
    else:
        print(arg_1)
        print(arg_2)
        print(arg_3)
        print(arg_4)
print(func_2(50))

print("#"*80)

def func_3(arg1, arg2=None, *args):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(f"args: {args}")
    print(f"type of args: {type(args)}")

print(func_3(10,"hello", 1,2,3,4,5,True,None,"Python",key_1 = "value1", key_2 = 1000))


dict_workers = {'mark':1000, 'jones':2500, 'Anna':2000, "Maria":3000, "Sofia":1500 }
def sort_workers(worker_dict):
    str = dict()
    for key in sorted(workers):
        str[key] = workers[key]
    print(str)
print(sort_workers(dict_workers))
