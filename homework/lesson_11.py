print('and:')
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print()

print('or:')
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print()

print('not:')
print(not False)
print(not True)
print()


a = True
b = False
c = True
f = a and not b or c or (a and (b or c))


a = 2
b = 5

print(a < b)
print(b > 3)
print(a <= 2)
print(b >= 7)
print(a < 3 < b)
print(a == b)
print(a != b)
print(a is b)
print(a is not b)


# Майже всі порівняння дають очікувані логічні значення.
# (is / is not)перевіряють ідентичність об’єктів у пам’яті, а не просто рівність значень, тому для чисел зазвичай використовують == і !=.


print(f)