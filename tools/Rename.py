# -*- coding: utf-8 -*-
# Author: Misa
# Date: 2022-09-10 17:14
# LastEditTime: 2022-11-17 12:06
# LastEditors: Misa
# Description: Misa is my game's id
#

import multiprocessing as double
import os
import re
import sys

def filter_data(data):
    suffix_list = [".str",".mkv",".mp4",".ass"]
    for i in range(len(suffix_list)):
        if str(data) == str(suffix_list[i]):
            return True

#* 自动选集
def slet_num(a,b):
    num = list(set(a)^set(b))
    if a.count(num[0]) >= 1:
        return a.index(num[0])
    else:
        return b.index(num[0])

#* 检测程序
def write(path):
    #* 获取该路径下所有文件的后缀名(不重复)
    fileList=os.listdir(path)
    suffixlist = []
    for i in range(len(fileList)):
        suffixlist.append(fileList[i][fileList[i].rfind('.'):])

    #* 过滤
    new_suffixlist = filter(filter_data,suffixlist)
    suffixlist = list(new_suffixlist)

    #* 去重
    suffix_list = suffixlist
    new_suffixlist=list(set(suffixlist))
    new_suffixlist.sort(key=suffix_list.index)
    suffixlist = new_suffixlist
    suffixlist

    #*取文件后缀 .XXX
    sub = suffixlist[0]
    suffix = suffixlist[0][suffixlist[0].rfind('.'):]

    #* 将该类型文件写入txt
    os.makedirs(path + '/log', exist_ok=True)
    newfileList = []
    for n in range(len(suffixlist)):
        suffix = suffixlist[n][suffixlist[n].rfind('.'):]
        for i in range(len(fileList)):
            oldfileList = fileList[i]
            if oldfileList[oldfileList.rfind('.'):] == suffix:
                newfileList.append(oldfileList)

        file_max = len(newfileList)
        print("总共有%s个%s文件。" %(str(file_max),str(suffix)))
        with open(path+'\log\\' + suffix[1:len(suffix)] + 'log.txt','w',encoding='utf-8') as file:
            file.truncate()
            for i in range(int(file_max)):
                file.write(newfileList[i]+"\n")
        newfileList.clear()
    return suffixlist,file_max


#* 读取程序
def rename(path,suffix,file_max,offset,video):
    fileList = []
    video = video[1:len(video)-1]
    if len(str(file_max)) < 2:
        file_max = 2
    else:
        file_max = len(str(file_max))

    #* 读取指定文件
    with open(path,'r',encoding='utf-8') as file:
        fileList = file.readlines()

    #* 去掉 \n
    change = 0
    for change in range(len(fileList)):
        oldsub = fileList[change]
        fileList[change] = oldsub[0:len(oldsub)-1]

    #* 回到文件路径
    path = path[0:path.rfind('\log')]

    #* 用判断集数
    slet = slet_num(re.findall(r"-?\d+\.?\d*e?-?\d*?",fileList[0]),re.findall(r"-?\d+\.?\d*e?-?\d*?",fileList[1]))
    for i in range(len(fileList)):
        supfileList = re.findall(r"-?\d+\.?\d*e?-?\d*?",fileList[i])
        sets = supfileList[slet]
        high = fileList[i][0:fileList[i].rfind(sets)]
        low = fileList[i][fileList[i].rfind(sets)+len(sets):len(fileList[i])]
        stdname = high + str(sets) + low
        with open(path + "\log\log.txt",'a',encoding='utf-8') as test:
            for n in range(len(fileList)):
                if fileList[n] == high + str(sets) + low:
                    oldname=path + os.sep + fileList[n]  # os.sep添加系统分隔符
                    #设置新文件名
                    num = float(sets) - float(offset)
                    num = '{:g}'.format(num)
                    num = str(num)
                    newname=path + os.sep + video + "[" + num.rjust(file_max,"0") + "]" + str(suffix)
                    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
                    test.write(str(fileList[n])+" ====> "+ str(video) + "[" + num.rjust(file_max,"0") + "]" + str(suffix) + "\n")
                    break

def main(path,new_name,offset):
    path = path[1:len(path)-1]

    #* 启动检测
    text = write(path)
    file_max = text[1]
    text = list(text[0])
    print("已读取该目录下所有文件")

    #* 启动重命名程序
    for i in range(len(text)):
        suffix = text[i]
        fpath = path+'\log\\'+str(text[i][1:]) + "log.txt"
        rename(fpath,suffix,file_max,offset,new_name)
    print("已完成所有转换")

if __name__ == "__main__":
    #* 接受命令行参数
    path = str(sys.argv[1])
    new_name = str(sys.argv[2])
    offset = int(sys.argv[3])
    main(path,new_name,offset)
