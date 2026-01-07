aim = 67
guess = 0
while aim != guess:
    guess = int(input("请输入你猜的数字:"))
    if guess > aim :
        print("猜大了")
    elif guess < aim :
        print("猜小了")
    else :
        print("猜对了")
        break

print("程序结束")