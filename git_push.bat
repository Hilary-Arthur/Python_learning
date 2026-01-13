@echo off
chcp 65001 > nul 2>&1  :: 设置编码为 UTF-8，避免中文乱码
setlocal enabledelayedexpansion

:: 检查是否在 Git 仓库目录下
git rev-parse --is-inside-work-tree > nul 2>&1
if errorlevel 1 (
    echo 错误：当前目录不是 Git 仓库！
    pause
    exit /b 1
)

:: 提示用户输入提交信息
set /p commit_msg=请输入本次提交的备注信息（不能为空）：

:: 检查提交信息是否为空
if "!commit_msg!"=="" (
    echo 错误：提交信息不能为空！
    pause
    exit /b 1
)

echo.
echo ===================== 开始执行 Git 操作 =====================
echo.

:: 1. 添加所有修改的文件
echo 1. 执行 git add .
git add .
if errorlevel 1 (
    echo 错误：git add 操作失败！
    pause
    exit /b 1
)

:: 2. 提交代码
echo 2. 执行 git commit
git commit -m "!commit_msg!"
if errorlevel 1 (
    echo 错误：git commit 操作失败（可能没有需要提交的修改）！
    pause
    exit /b 1
)

:: 3. 拉取远程最新代码（避免推送冲突）
echo 3. 执行 git pull origin master
git pull origin master
if errorlevel 1 (
    echo 警告：git pull 操作失败（可能远程无 master 分支或网络问题），尝试直接推送...
)

:: 4. 推送到远程仓库
echo 4. 执行 git push origin master
git push github master
git push gitee master
git push gitnode master
if errorlevel 1 (
    echo 错误：git push 操作失败！
    pause
    exit /b 1
)

echo.
echo ===================== Git 操作执行完成 =====================
echo 提交信息：!commit_msg!
echo 推送分支：master
pause
endlocal