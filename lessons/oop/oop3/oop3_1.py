class Plant:

    model = "T-64BV"
    speed = 50
    muzzle = 3
    thickness = 5

    def __init__(self, model, speed, muzzle, thickness):
        self.model = model
        self.speed = speed
        self.muzzle = muzzle
        self.thickness = thickness

    def __str__(self):
        return f"Tank info: model:{self.model}, speed:{self.speed}, muzzle:{self.muzzle}, thickness:{self.thickness}"


    def shot(self):
        return "Boom!!!"

    def move(self):
        return "Tank is moving..."

    def oil(self):
        return "Tank with fool oil..."

    def watt(self):
        count = 0
        for i in range(1000):
            count += 1
        return f"Tank is working... (interations): {count}$"




T_72 = Plant("T-72", 80, 2.9, 4.5)
T_90 = Plant("T-90", 40, 3.5, 6)

print(T_72,'\n', T_90)
# Tank_2 = Plant()
# Tank_2.model = "T-72"
# Tank_2.speed = 80
# Tank_2.muzzle = 2.9
# Tank_2.thickness = 4.5
#
# Tank_3 = Plant()
# Tank_3.model = "T-90"
# Tank_3.speed = 40
# Tank_3.muzzle = 3.5
# Tank_3.thickness = 6
