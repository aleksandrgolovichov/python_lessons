my_note = open("../lesson_17/nyte.txt", "r")
content = my_note.read()
for i in content:
    print(content[i])
content = eval(content)
print(type (content))
print(type(content[-1]))
print("SET, set(content))")
for i in content:
    print(i)
my_note.close()