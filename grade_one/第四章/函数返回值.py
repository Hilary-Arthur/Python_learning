import random

def add (a,b):
    '''
    :param a: 形参a表示相加的其中一个数字
    :param b:
    :return:
    '''
    result = a + b
    return result

a = random.randint(1,100)
b = random.randint(1,100)
result = add(a,b)
print(f"{a}+{b}={result}")

def none_return():
    print()

print(none_return())
print(type(none_return()))