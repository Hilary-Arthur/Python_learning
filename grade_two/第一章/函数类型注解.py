import random


def test_1(data: list,num: int):
    while num > 0:
        print(data[num-1],end=" ")
        num -= 1

def get_list(num: int) -> list:
    tmp = list()
    while num > 0:
        tmp.append(random.randint(1,100))
        num -= 1
    return tmp

if __name__ == '__main__':
    data = get_list(10)
    test_1(data,len(data))