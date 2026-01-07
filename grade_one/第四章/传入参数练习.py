def input_number_judge(data):
    if data > 18 :
        print("恭喜您，成年了")
    else :
        print("您无需购买成人票")

data = int(input("请输入您的年龄"))
input_number_judge(data)