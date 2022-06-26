#!/usr/bin/env python3
# 使用系统默认的 python3 运行
###########################################################################################
# 作者：gfdgd xi
# 版本：1.4.1
# 更新时间：2022年06月22日
# 感谢：感谢 wine 以及 deepin-wine 团队，提供了 wine 和 deepin-wine 给大家使用，让gfdgd xi能做这个程序
# 基于 Python3 的 tkinter 构建
###########################################################################################
#################
# 引入所需的库
#################
import os

###################
# 程序功能
###################
print("请保证你能有 root 权限以便安装")
print("如果有请按回车，否则按 [Ctrl+C] 退出", end=' ')
input()
os.system("sudo apt update")
print("请问是否要更新操作系统？[Y/N]", end=' ')
choose = input().upper()
if not choose == "N":
    os.system("sudo apt upgrade -y")
print("请你务必安装 apt-fast（需要添加星火应用商店的源）？[Y/N]", end=' ')
choose = input().upper()
if not choose == "N":
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo apt install apt-fast -y")
    if not os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo touch /etc/apt/sources.list.d/sparkstore.list")
        os.system("echo 'deb [by-hash=force] https://d.store.deepinos.org.cn/ /' | sudo tee '/etc/apt/sources.list.d/sparkstore.list'")
        os.system("sudo apt update")
    os.system("sudo apt install apt-fast -y")
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo apt update")
print("请问是否要安装 spark-wine7-devel（需要添加星火应用商店的源）？[Y/N]", end=' ')
choose = input().upper()
if not choose == "N":
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo ss-apt-fast install spark-wine7-devel -y")
    if not os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo touch /etc/apt/sources.list.d/sparkstore.list")
        os.system("echo 'deb [by-hash=force] https://d.store.deepinos.org.cn/ /' | sudo tee '/etc/apt/sources.list.d/sparkstore.list'")
        os.system("sudo apt update")
    os.system("sudo ss-apt-fast install spark-wine7-devel -y")
    if os.path.exists("/etc/apt/sources.list.d/sparkstore.list"):
        os.system("sudo apt update")
print("全部完成！")
