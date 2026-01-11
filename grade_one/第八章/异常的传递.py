def func_1():
    print("执行函数1:1/0，会出现异常")
    num = 1 / 0
    print("函数1结束")

def func_2():
    print("函数2开始")
    func_1()
    print("函数2结束")

def main():
    try :
        func_2()
    except Exception as e:
        print(f"函数2出现的异常被main函数接收：{e}")

main()