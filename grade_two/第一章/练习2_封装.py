# 设计一个手机类，包含私有成员变量__is_5g_enable,类型bool,True表示开启,False表示关闭
# 私有成员方法:__check_5g()，会判断私有成员变量的值
# True打印5g开启，反之打印5g关闭，使用4g网络
# 公开成员方法:call_by_5g()，调用其执行:
# 1.调用私有成员方法:__check_5g()，判断5g网络状态
# 2.打印输出正在通话中
# 运行结果5g关闭,使用4g网络
# 正在通话中
import random


class Phone:
    __is_5g_enable = bool(random.randint(0,1))
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else :
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

if __name__ == '__main__':
    phone = Phone()
    phone.call_by_5g()