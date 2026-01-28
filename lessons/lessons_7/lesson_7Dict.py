print("Dict")
dict_info = {
    "day": 'monday',
    "month": 'january',
    "year": 2024,
    'temperature': -10,
    "wether": 'snow',
    "city": 'Kyiv',
    "contry": 'contry',
 }
print("city" in dict_info)
hobby = ["football", "programming","chess"]
all_person = []
person = {
    "name": "Sasha",
    "age":15,
    "form":9,
    "hobby": hobby[2],
    "is_student": True,
}

other_person = dict(name="bob", age=18, form=12)

print(dict_info)
print(person)

all_person.append(person)
all_person.append(other_person)
print(all_person)

# person = (owner_car) = "BMW"
# person = (is_woring) = True
print(dict_info.keys())
print(dict_info.values())
print(list(dict_info.items())[-1])
del person["form"]
del person["is_student"]

print(person)
print(person.__dir__())