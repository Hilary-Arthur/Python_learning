def get_left(name,money):
    print(f"{name}剩余的余额为{money}")

def raise_money(name,delta):
    global money
    money += delta
    print(f"{name}账户存入{delta}的钱，当前余额{money}")

def get_money(name,delta):
    global money
    if money - delta < 0:
        print("您的余额不足")
        return 0
    else :
        money -= delta
        print(f"{name}账户成功取出{delta}元，账户余额{money}")
        return 1

def menu(name):
    print(f"======{name}用户======")
    print("\t1.\t查询余额")
    print("\t2.\t存款")
    print("\t3.\t取款")
    print("\t4.\t退出")
    print("===================")

def main(name):
    global money
    # 此处应为全局变量money才能够确保get_left中的钱准确
    answer = 1
    while answer :
        menu(name)
        answer = int(input("请选择您要执行的操作:"))
        if answer == 4 :
            break
        elif answer == 1:
            get_left(name,money)
        elif answer == 2:
            delta = int(input("请输入存入的钱的数额"))
            raise_money(name,delta)
        else :
            delta = int(input("请输入取出的钱的数额"))
            answer = get_money(name,delta)
        if answer == 0 :
            print("出现错误，程序结束")
            break

name = "Tom"
money = 10000
main(name)