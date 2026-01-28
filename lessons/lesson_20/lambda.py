def double(x):
    return x * 2

print(double(40))
double_lambda = lambda x: x * 2
print(double_lambda(40))

def test(x, y):
    return x * y + y*x*(x**2)/y
print(test(2, 3))

test_lambda = lambda x, y: x * y + y * x * (x ** 2) / y
print(test_lambda(2, 3))

def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(10, 20))