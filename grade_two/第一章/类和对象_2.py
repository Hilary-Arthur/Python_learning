import winsound


class Clock:
    id = None
    price = None

    def ring(self):
        winsound.Beep(2000,3000)

# 创建对象
clock_1 = Clock()
clock_2 = Clock()
clock_1.id = "0000001"
clock_1.price = 21.99
print(f"闹钟ID:{clock_1.id},闹钟价格{clock_1.price}")
clock_1.ring()