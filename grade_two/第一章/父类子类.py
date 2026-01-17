class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("父类的5g通话")

class My_Phone(Phone):
    producer = "ITHEIMA"
    def call_by_5g(self):
        # 方法1
        # print(f"在子类中调用父类的厂商:{Phone.IMEI}")
        # print("在子类中调用父类方法:",end="")
        # Phone.call_by_5g(self)
        # 方法2
        print(f"在子类中调用父类的厂商:{super().producer}")
        print("在子类中调用父类方法:", end="")
        super().call_by_5g()
        print(f"子类的厂商:{self.IMEI}")
        print("子类的5g通话")

if __name__ == '__main__':
    phone = My_Phone()
    # 执行的应该是子类的方法
    phone.call_by_5g()
    print(phone.producer)