num = 100
def test_1():
    print(f"test_1:{num}")

def test_2():
    # num = 200
    # 局部变量，外部不变，解决方法将num变为global全局变量
    global num
    num = 200
    print(f"test_2:{num}")

test_1()
test_2()
print(num)