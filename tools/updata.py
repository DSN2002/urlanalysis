# -*- coding: utf-8 -*-
# Author: Misa
# Date: 2022-09-26 20:22
# LastEditTime: 2022-11-17 00:26
# LastEditors: Misa
# Description:
# 仅供研究使用，请勿用于其他活动
#

import multiprocessing as double
import re
import os

def down_updata_check(path):
    url = "https://gitee.com/DSN2002/urlanalysis/releases/tag/urlanalysis"
    os.system(path+"\\tools\\management.bat 1 " + url)

def down_updata():
    url = "https://gitee.com/DSN2002/urlanalysis/releases/download/urlanalysis/version.txt"
    os.system(path+"\\tools\\management.bat 2 " + url)

def cmp_versions(path,local_vre):
    with open(path+"\\tools\\updata\\check.txt",'r',encoding='utf-8') as online_text:
        for i in range(4):
            online_vre = online_text.readline()                 #* 获取网络版本的版本
    online_vre = re.findall(r"\d+.\d+.\d+",online_vre)
    online_vre = online_vre[0]
    if str(local_vre) == str(online_vre):
        print("当前版本是最新版本")
    else:
        print("当前最新版本为：%s\n正在下载更新" %online_vre)



def main(local_vre):
    path = os.getcwd()
    cmp_versions(path,local_vre)

if __name__ == "__main__":
    #multiprocessing.freeze_support()                 #* 让打包程序识别这个是多进程文件
    main()
