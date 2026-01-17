# 手机功能'
class Function_phone:
    ans = None
    producer = "Itcast"
    def chooce_func(self):
        if self.ans != 0:
            print("正在选择功能")
# 单继承
class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g通话")
# 继承了Phone和Function_phone多个类
class Phone2026(Function_phone,Phone):
    face_id = "101110"
    def call_by_5g(self):
        print("2026年新增功能:5g通话")

if __name__ == '__main__':
    phone = Phone2026()
    # 存在相同的变量时，遵循左侧优先，即先被继承的那个类中的变量被打印，方法同理
    print(phone.producer)
    phone.call_by_5g()
    # 能够调用其继承过来的功能
    phone.call_by_4g()
    phone.ans = 1
    phone.chooce_func()