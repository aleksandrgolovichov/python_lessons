
class person:

    kind = "human"
    live = "earth"

    def __init__(self,sex, name, age, city, status):
        self.name = name
        self.sex = sex
        self.age = age
        self.city = city
        self.status = status


    def __str__(self):
        return f"person: name:{self.name},age:{self.age}, city:{self.city}, status:{self.status}"

    def breath(self):
        return "breathing..."

    def run(self):
        return "run..."

    def eat(self):
        return "eating..."

    def sleep(self):
        return "sleeping..."

    def work(self):
        count = 0
        for i in range(1000):
            count += 1
        return f"working... (interations): {count}$"


# person_1 = person('sex', 'name', 'age', 'city', and 'status')
# person_2 = person('sex', 'name', 'age', 'city', and 'status')
# print(person_1.kind)
# print(person_1.breath())
# print(person_1.run())
# print(person_1.eat())
# print(person_1.sleep())
# print(person_1.work())


Masha = person("femele","Masha", 25, "  Ukraine", "single")
Sasha = person("male","Sasha", 30, "Ukraine", "married")
Polina = person("femele","Polina", 28, "Ukraine", "single")
Mikola = person("male","Mikola", 35, "Ukraine", "married")
Alex = person("male","Alex", 40, "Ukraine", "married")
Aliona = person("femele","Aliona", 22, "Ukraine", "single")

print(Masha.work())
print(Sasha.run())
print(Polina.eat())
print(Mikola.sleep())



print(Masha,'\n', Sasha,'\n' ,Polina,'\n' ,Mikola,'\n' ,Alex,'\n' ,Aliona)

# print(type(person_1))
# print(type(person_2))
#
# print(id(person_1))
# print(id(person_2))

# number_1 = 10
# number_2 = 10
# print(type(number_1))
# print(type(number_2))
# print(id(number_1))
# print(id(number_2))