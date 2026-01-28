empty_list = []
for i in range(10):
    if i % 2 == 1:
        empty_list.append(i*i)
    else:
        empty_list.append(1+2)
print(empty_list)

empty_list = [i * i if i % 2 == 1 else 1 + 2 for i in range(10)]
print(empty_list)


d = {}
for i in range(1,13):
    if i % 2 == 1:
        d[i] = i*i
print(d)

d = {i: i*i for i in range(1, 13) if i % 2 == 1}
print(d)


d2 ={}
for num in range(1,13):
    if num % 21:
        d2 [num] = num*2
    else:
        d2 [num] = num/0.5
print(d2)

d2 = {num: num*2 if num % 21 else num/0.5 for num in range(1, 13)}
print(d2)