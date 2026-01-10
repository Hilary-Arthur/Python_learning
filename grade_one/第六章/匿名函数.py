# 函数作为参数传递
def test_func(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x+y

test_func(compute)

'''
    函数compute,作为参数,传入了test_func中使用
    这是计算逻辑的传递，而非数据的传递
'''

# lambda匿名函数,无法二次使用,且无法写多行
test_func(lambda x,y:x+y)