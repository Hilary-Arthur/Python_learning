# 异常

## 了解异常
+ 当程序检测到一个错误时，Python解释器就无法继续执行了，反而出现了一些错误提示，即“异常 ”
## 异常捕获的办法（异常处理）
+ 基本语法：
  + ```
        try:
            可能发生错误的代码
        except:
            如果出现异常执行的代码
    ```
+ 捕获指定异常
  + 基本语法：
    + ```
          try:
              print(name)
          except NameError as e:
              print('name变量名称未定义错误')
      ```
+ 注意：
  + 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
  + 一般try下方只放一行尝试执行的代码
+ 捕获多个异常
  + 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
  + ```
        try:
            print(1/0)
        except (NameError,ZeroDivisionError):
            print('ZeroDivision错误...')
    ```
+ 捕获所有异常
+ 异常else
  + 表示如果没有异常要执行的代码
+ finally表示无论有没有异常都会执行
## Python模块

## Python包

## 安装第三方Python包