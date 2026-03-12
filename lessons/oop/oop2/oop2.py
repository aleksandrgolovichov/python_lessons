

class Fruits:
    name = "cherry"
    color = "red"
    taste = "sour"

    def apple_funk(self):
        print(f"apple have {self.taste} taste")

apple = Fruits()
apple.name = "apple"
apple.color = "green"
apple.taste = "sweet"
apple.apple_funk()


banana = Fruits()
banana.name = "banana"
banana.color = "yellow"
banana.taste = "sweet"

print(f"At home i have a {banana.name} with {banana.color} color and {banana.taste} taste")


class Vegetables:
    name = "carrot"
    color = "orange"
    taste = "sweet"

    def say_hello(self):
        print("Hello, World!")
        return "Greeting has been printed."

    def carrot(self):
        print(f"carrot have {self.color} color")

carrot = Vegetables()
carrot.carrot()
carrot.say_hello()
print(type(carrot))
potato = Vegetables()
potato.name = "potato"
potato.color = "yellow"
potato.taste = "tart"

cabbage = Vegetables()
cabbage.name = "cabbage"
cabbage.color = "green"
cabbage.taste = "fresh"

print(f"At home i have a {potato.name} with {potato.color} color and {potato.taste} taste")

def say_hello():
    print("Hello, World!")
    return "Greeting has been printed."
say_hello()
print(type(say_hello))

name = "Sasha"
print(name.upper())
age = "Sasha"
print(id(name))
print(type(name))
print(type(age))
print(id("Sasha"))
print(type(str()))
print(type(carrot))

class Pupil:
    name = "abc"
    age = 15
    country = "Ukraine"

    # def upper_name(self):
    #     # text0110 0001 = "A"
    #     list_bits = ["01100001","01100010", "01100011", "01100100", "01100101", "01100110", "01100111", "01101000", "01101001", "01101010",]
    #     list_up_bits = ["01000001","01000010", "01000011", "01000100", "01000101", "01000110", "01000111", "01001000", "01001001", "01001010",]
    #     dict_upper = dict(zip(list_bits, list_up_bits))
    #     print(dict_upper)
    #     bits = ''.join(format(byte, '08b') for byte in Pupil.name.encode('utf-8'))
    #     list_bit = bits.split(',')
    #     print(list_bit)
    #     print(bits)
    #     # print(bits)
    #
    #     for i in list_bit:
    #         if i in dict_upper:
    #             print(dict_upper[i])


                # if bits == "01100001,01100010,01100011":
        #      return "A"
        # else:
        #     return "not A"



        # print(bits)
        # return "A"




# person = Pupil()
# print(id(person))
# print(type(person))
# print(person.upper_name())
#
# # text = "а"
# # byte_data = text.encode('utf-8')
# # print(byte_data)
#
# bit_string = "010000010100001001000011" # Це "Hi" у бітах
#
# # 1. Розбиваємо рядок на частини по 8 біт
# # 2. Перетворюємо кожну частину на ціле число (int з основою 2)
# # 3. Створюємо об'єкт bytes і декодуємо його в текст
# byte_data = bytes(int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8))
# text = byte_data.decode('utf-8')
#
# print(text)

dict_upper = {
    "01100001": "01000001",
    "01100010": "01000010",
    "01100011": "01000011",
    "01100100": "01000100",
    "01100101": "01000101",
    "01100110": "01000110",
    "01100111": "01000111",
    "01101000": "01001000",
    "01101001": "01001001",
    "01101010": "01001010",
    "01101011": "01001011",
    "01101100": "01001100",
    "01101101": "01001101",
    "01101110": "01001110",
    "01101111": "01001111",
    "01110000": "01010000",
    "01110001": "01010001",
    "01110010": "01010010",
    "01110011": "01010011",
    "01110100": "01010100",
    "01110101": "01010101",
    "01110110": "01010110",
    "01110111": "01010111",
    "01111000": "01011000",
    "01111001": "01011001",
    "01111010": "01011010"
}

name = "apple!"

bits = ''.join(format(byte, '08b') for byte in name.encode())
list_bit = [bits[i:i+8] for i in range(0, len(bits), 8)]

result = ""

for i in list_bit:
    if i in dict_upper:
        upper_bits = dict_upper[i]
        letter = chr(int(upper_bits, 2))
    else:
        letter = chr(int(i, 2))

    result += letter

print(result)