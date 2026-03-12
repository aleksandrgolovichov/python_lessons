bananas = 44
# Integer
print(type(bananas))
apples_kg = 2.5
# float
print(type(apples_kg))
name_apples = "Green Apples"
# string
print(type(name_apples))
in_market = True
# Boolean
print(type(in_market))
ather_kandys = ["shokolapki", "iriski","rachok", "Barbarisy","dushes"]
for kandys in ather_kandys:
    print(kandys)
# list
print(type(ather_kandys))
ather_kandys.append("marmeladky")
ather_kandys.remove("iriski")
print(ather_kandys)
kandys_price_grn =   {
    "shokolapki": 15,
    "iriski":19,
    "rachok":13,
    "barbarisky":17,
    "dushes":21
}
# dictionary
kandys_price_grn["marmeladky"]= 25
kandys_price_grn.pop("iriski")
kandys_price_grn.update({"barbarisky":18})
for kays,values in kandys_price_grn.items():
    print(f"kays:{kays}, Values:{values}")
print(kandys_price_grn)
print(type(kandys_price_grn))
famus_shop = ("atb", "silpo","novus", "Fora")
# tuple
for shops in famus_shop:
    print(shops)
owners_makets = {"Vasiliy Gorbuzatin", "Petro Poroshenko", "Ivan Savun","Vasiliy Gorbuzatin", "Petro Poroshenko", "Ivan Savun",10,10,10,10,10}
# set
owners_makets.remove(10)
owners_makets.add("Oleg Blokhin")
for owners in owners_makets:
    print(owners)
print(owners_makets)


def my_funk(people):
    ather_kandys.extend(people)
    return ather_kandys
my_funk(famus_shop)
my_funk(famus_shop)
print(ather_kandys)

def my_funk2(p1,p2,p3):
    result = p1+p2+p3
    return result/3
my_funk2(20,812,39)
print(my_funk2(20,812,39))

def my_funk3(n1,n2):
    result = n1+n2
    return result
print(my_funk3(200,800))



