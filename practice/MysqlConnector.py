import random
from faker import Faker

import mysql
import mysql.connector as connector



def mysql_Conn():
    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "raojiarui0601",
        database = "python",
        port = "3306"
    )
    cursor = db.cursor()
    return db,cursor

def insert_user(cursor,name,age):
    if cursor.execute(f"INSERT INTO test_1(name,age)VALUES('{name}','{age}')"):
        print("输入插入成功")

def select_user(cursor,name,age):
    if name != 0 and age == 0:
        cursor.execute(f"SELECT * FROM test_1 WHERE name = {name}")
    elif name == 0 and age != 0:
        cursor.execute(f"SELECT * FROM test_1 WHERE age = {age}")
    elif name != 0 and age != 0:
        cursor.execute(f"SELECT * FROM test_1 WHERE name = {name} AND age = {age}")
    else :
        cursor.execute("SELECT * FROM test_1")
    rs = cursor.fetchall()
    return rs




def main():
    db,cursor = mysql_Conn()
    # try :
    #     fake = Faker()
    #     i = 0
    #     while i < 20:
    #         name = fake.name()
    #         age = random.randint(0,100)
    #         insert_user(cursor,name,age)
    #         i += 1
    #     db.commit()
    # except Exception as e:
    #     print(f"操作出错: {e}")
    #     db.rollback()  # 回滚事务
    print("数据插入完毕，执行查找操作")
    key = int(input("请输入查询的年龄:"))
    rs = select_user(cursor,0,0)
    for row in rs:
        print(row)
    if cursor:
        cursor.close()
    if db.is_connected():
        db.close()
main()