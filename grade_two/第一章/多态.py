class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()


if __name__ == '__main__':

    dog = Dog()
    cat = Cat()

    make_noise(dog)
    make_noise(cat)

# 演示抽象类
class AC:
    def cool_wind(self):
        # 制冷
        pass

    def hot_wind(self):
        # 制热
        pass

    def swing_l_r(self):
        # 左右摆风
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的冷风制冷系统")

    def hot_wind(self):
        print("美的制热系统")

    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力冷风制冷系统")

    def hot_wind(self):
        print("格力制热系统")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_l_r()

if __name__ == '__main__':
    ac_1 = Midea_AC()
    ac_2 = GREE_AC()

    make_cool(ac_1)
    make_cool(ac_2)