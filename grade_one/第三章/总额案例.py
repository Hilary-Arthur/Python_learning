# 发工资问题
# 员工编号1-20，从编号编号1开始，依次领取工资，每人可领1000元
# 领工资时，财务判断员工绩效分（1-10）随机生成，如果低于5，不发工资，如果工资发完了结束发工资
import random

origin_people = 20
money = 10000
for i in range(1,origin_people+1):
    num = random.randint(1,10)
    if num < 5:
        print(f"第{i}位员工绩效分{num},不发工资")
        continue
    if money <= 0:
        print("没钱了，不发了")
        break
    money -= 1000
    print(f"第{i}位员工绩效分{num},发工资1000元,剩余{money}元")
