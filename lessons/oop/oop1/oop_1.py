# ООП - 06'єктно-орієнтоване програмування
# Клас - це шаблон для створення об'єктів. Він визначає властивості та методи, які будуть спільними для всіх об'єктів цього класу.
# 06'єкт - це конкретний екземпляр класу, який має свої власні властивості та може виконувати методи, визначені в класі.
# import datetime
#
# print(sum([1,2,3]))
#
# some_list = [1, 2, 3, 4, 5]
# print(type(some_list))
# some_list.append(6)
# print(some_list)
#
# name = "John"
# print(type(name))
# print(str.__dict__)
#
# class car:
#     model = "Toyota" #властивість класу
#     engine = "2.5l" #властивість класу
#
#
# car_1red = car() #створення об'єкта класу car
# print(type(car_1red))
# car_2red = car()
# car_3green = car()
# car_4grey = car()
# car_5blue = car()
#
# print(type(car_5blue.model))
# print(type(car_5blue.engine))
#
# class person:
#     "this is a class for person"
#
#     name = "John"
#     age = 30
#     city = "New York"
#
# def about_self(self):
#     print(f"name: {self.name}, age: {self.age}, city{self.city}, time: {self.checkTime()}")
#
# def checkTime(self)
#     current_time = datetime.datetime.now().time()
#     return current_time
#
#
# def printInfo(self):
#     print("Hello from person")
# print(person.name)
# print(person.age)
# print(person.city)
#
# person.name = "Sasha"
# print(person.name)
#
# girl = person()
# girl.name = "Anna"
# girl.age = 22
# print(f"name: {self.name}, age: {self.age}, city{self.city}")
# print(person.name)
#
# print(person.__dict__)
# print(girl.__dict__)
# print(person.__doc__)
# # print(type(girl))
# # print(isinstance(girl, car))
# # print(isinstance("Hello", car))






class Pet:
    name = "Bob"
    live = "in house"
    eat = "fish"

Cat_Pet = Pet()

Hamster_Pet = Pet()
Hamster_Pet.name = "jack"
Hamster_Pet.eat = "cucmber"

Pig_Pet = Pet()
Pig_Pet.name = "Anna"
Pig_Pet.live = "Outdoor"
Pig_Pet.eat = "corn"

print(f"I have a pet cat {Cat_Pet.name}, hamster {Hamster_Pet.name} and pig {Pig_Pet.name}")



class Animal:
    name = "wolf"
    color = "grey"
    eat = "meat"

    def wolf_language(self):
        print("woof-woof")


    def bear_language(self):
        print("grrrr")


wolf = Animal()
wolf.wolf_language()

bear = Animal()
bear.name = "bear"
bear.color = "brown"
bear.eat = ("honey", "fish", "meat")
bear.bear_language()

fox = Animal()
fox.name = "fox"
fox.color = "orange"
fox.eat = "meat"


print(f" My favorite animal is a {bear.name} after the {wolf.name} and {fox.name}")







