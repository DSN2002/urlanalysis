# -*- coding: utf-8 -*-
# Author: Misa
# Date: 2022-09-26 20:22
# LastEditTime: 2022-11-17 20:49
# LastEditors: Misa
# Description:
# 仅供研究使用，请勿用于其他活动
#

import tkinter as tkk
import tkinter.filedialog
import tkinter.ttk # 导入ttk模块，下拉菜单控件位于ttk子模块中
import multiprocessing as double
import sys
import re
import os
from tools import updata
from tools import Rename

def Anime4K_setting_Command():

    #* 获得设置文件,将设置读取到列表中
    Anime4K_setting_path = os.getcwd() #*获取路径
    Anime4K_setting_path = Anime4K_setting_path + "\MPV\portable_config\input.conf"
    Anime4K_setting_List = []
    #* 读取指定文件
    with open(Anime4K_setting_path,'r',encoding='utf-8') as file:
        Anime4K_setting_List = file.readlines()
    #* 去掉 \n
    change = 0
    for change in range(len(Anime4K_setting_List)):
        oldsub = Anime4K_setting_List[change]
        Anime4K_setting_List[change] = oldsub[0:len(oldsub)-1]
    change = 0
    anime4K_open = 0
    anime4K_close = 0
    for change in range(len(Anime4K_setting_List)):
        if Anime4K_setting_List[change][0:6] == "CTRL+0":
            anime4K_close = change
            #print(Anime4K_setting_List[anime4K_close])
        if Anime4K_setting_List[change][0:6] == "CTRL+1":
            anime4K_open = change
            #print(Anime4K_setting_List[anime4K_open])

    #* 着色器处理函数
    def shaders_match(strings,text):
        shaders_num = strings.find(text)
        #print(shaders_num)
        if shaders_num == -1:
            return ""
        else:
            text_strings = strings[shaders_num-8:]
            return text_strings[0:text_strings.find(".glsl")]

    #* 窗口设置部分

    top = tkk.Toplevel()
    top.title("Anime4K着色器配置")
    top.config(bg='#87CEEB')
    width = 800
    height = 600
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height,(screenwidth-width)/2,(screenheight-height)/2)
    top.geometry(size_geo)
    top.attributes('-topmost',True)
    icon_path = os.getcwd()
    icon_path = icon_path + "\document\\analysis.ico"
    top.iconbitmap(icon_path)

    #* 建立一个显示原来的着色器队列的文本框
    old_shaders_text = tkinter.Text(top,bd=2)
    old_shaders_text.place(relx=0.25,rely=0.2,relheight=0.3,relwidth=0.25)
    #* 建立一个显示选择的着色器队列的文本框
    new_shaders_text = tkinter.Text(top,bd=2)
    new_shaders_text.place(relx=0,rely=0.2,relheight=0.6,relwidth=0.25)
    #* 建立一个存放新着色器队列的列表
    new_shaders_list = []

    new_shaders_activation = tkk.Label(top,text='选择的着色器栏',bg='#9AC0CD',font=('宋体',20))
    new_shaders_activation.place(relx=0,rely=0,relheight=0.2,relwidth=0.25)
    #* Restore
    # 在主窗口上添加一个frame控件
    frame1 = tkk.Frame(top,bg='#87CEEB',bd=2)
    frame1.place(relx=0.5,rely=0,relheight=0.25,relwidth=0.25)
    frame_Restore = tkk.Label(frame1,text='Restore着色器',bg='#87CEEB',font=('宋体',15))
    frame_Restore.place(relx=0,rely=0,relheight=0.5,relwidth=1)
    # 创建Restore着色器下拉菜单
    Restore_select_cbox = tkinter.ttk.Combobox(frame1)
    Restore_select_cbox.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
    # 设置下拉菜单中的值
    Restore_select_cbox['value'] = (
                        "无",
                        "Anime4K_Restore_CNN_UL",
                        "Anime4K_Restore_CNN_VL",
                        "Anime4K_Restore_CNN_L",
                        "Anime4K_Restore_CNN_M",
                        "Anime4K_Restore_CNN_S",
                        "Anime4K_Restore_CNN_Soft_UL",
                        "Anime4K_Restore_CNN_Soft_VL",
                        "Anime4K_Restore_CNN_Soft_L",
                        "Anime4K_Restore_CNN_Soft_M",
                        "Anime4K_Restore_CNN_Soft_S"
                        )
    #通过 current() 设置下拉菜单选项的默认值
    Restore_select_cbox.current(0)
    # 编写回调函数，绑定执行事件,向文本插入选中文本
    def Restore_select_input(event):
        new_shaders_list.append(Restore_select_cbox.get())
        new_shaders_text.insert('insert',Restore_select_cbox.get()+"\n")
    # 绑定下拉菜单事件
    Restore_select_cbox.bind("<<ComboboxSelected>>",Restore_select_input)

    #* Upscale
    frame2 = tkk.Frame(top,bg='#87CEEB',bd=2)
    frame2.place(relx=0.5,rely=0.25,relheight=0.25,relwidth=0.25)
    frame_Upscale = tkk.Label(frame2,text='Upscale图像放大器',bg='#87CEEB',font=('宋体',15))
    frame_Upscale.place(relx=0,rely=0,relheight=0.5,relwidth=1)
    Upscale_select_cbox = tkinter.ttk.Combobox(frame2)
    Upscale_select_cbox.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
    Upscale_select_cbox['value'] = (
                        "无",
                        "Anime4K_Upscale_CNN_x2_UL",
                        "Anime4K_Upscale_CNN_x2_VL",
                        "Anime4K_Upscale_CNN_x2_L",
                        "Anime4K_Upscale_CNN_x2_M",
                        "Anime4K_Upscale_CNN_x2_S"
                        )
    Upscale_select_cbox.current(0)
    def Upscale_select_input(event):
        new_shaders_list.append(Upscale_select_cbox.get())
        new_shaders_text.insert('insert',Upscale_select_cbox.get()+"\n")
    Upscale_select_cbox.bind("<<ComboboxSelected>>",Upscale_select_input)


    #* AutoDownscalePre
    frame_AutoDownscalePre = tkk.Frame(top,bg='#87CEEB',bd=2)
    frame_AutoDownscalePre.place(relx=0.75,rely=0,relheight=0.25,relwidth=0.25)
    frame_AutoDownscalePre_lable = tkk.Label(frame_AutoDownscalePre,text='AutoDownscalePre',bg='#87CEEB',font=('宋体',15))
    frame_AutoDownscalePre_lable.place(relx=0,rely=0,relheight=0.5,relwidth=1)
    AutoDownscalePre_select_cbox = tkinter.ttk.Combobox(frame_AutoDownscalePre)
    AutoDownscalePre_select_cbox.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
    AutoDownscalePre_select_cbox['value'] = (
                        "无",
                        "Anime4K_AutoDownscalePre_x2",
                        "Anime4K_AutoDownscalePre_x4"
                        )
    AutoDownscalePre_select_cbox.current(0)
    def AutoDownscalePre_select_input(event):
        new_shaders_list.append(AutoDownscalePre_select_cbox.get())
        new_shaders_text.insert('insert',AutoDownscalePre_select_cbox.get()+"\n")
    AutoDownscalePre_select_cbox.bind("<<ComboboxSelected>>",AutoDownscalePre_select_input)

    #* 附加组件
    frame_extra = tkk.Frame(top,bg='#87CEEB',bd=2)
    frame_extra.place(relx=0.75,rely=0.25,relheight=0.25,relwidth=0.25)
    frame_extra_lable = tkk.Label(frame_extra,text='附加组件',bg='#87CEEB',font=('宋体',15))
    frame_extra_lable.place(relx=0,rely=0,relheight=0.5,relwidth=1)
    extra_select_cbox = tkinter.ttk.Combobox(frame_extra)
    extra_select_cbox.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
    extra_select_cbox['value'] = (
                        "无",
                        "Anime4K_Thin_HQ",
                        "Anime4K_Thin_Fast",
                        "Anime4K_Thin_VeryFast",
                        "Anime4K_Darken_HQ",
                        "Anime4K_Darken_Fast",
                        "Anime4K_Darken_VeryFast",
                        )
    extra_select_cbox.current(0)
    def extra_select_input(event):
        new_shaders_list.append(extra_select_cbox.get())
        new_shaders_text.insert('insert',extra_select_cbox.get()+"\n")
    extra_select_cbox.bind("<<ComboboxSelected>>",extra_select_input)


    #* 当前已激活
    frame_activation = tkk.Frame(top,bg='#87CEEB',bd=2)
    frame_activation.place(relx=0.25,rely=0,relheight=0.2,relwidth=0.25)
    frame_activation_lable = tkk.Message(frame_activation,text='当前已激活着色器',bg='#87CEEB',width=180,font=('宋体',15))
    frame_activation_lable.place(relx=0,rely=0,relheight=1,relwidth=1)

    #* 说明栏
    help_frame = tkk.Frame(top,bg='#87CEEB',bd=2)
    help_frame.place(relx=0.25,rely=0.5,relheight=0.5,relwidth=0.75)
    help_frame_lable = tkk.Label(help_frame,text='着色器使用说明',bg='#9AC0CD',font=('宋体',20))
    help_frame_lable.place(relx=0,rely=0,relheight=0.2,relwidth=1)
    help_frame_lable1 = tkk.Label(help_frame,text="加载顺序"+"\n"+"Restore + Upscale + (Restore) + AutoDownscalePre + (Upscale) + 附加组件"+"\n"+"括号中的加不加看自己显卡性能",bg='#9AC0CD',font=('宋体',12))
    help_frame_lable1.place(relx=0,rely=0.2,relheight=0.2,relwidth=1)
    help_frame_lable1 = tkk.Label(help_frame,text="Restore用于去除压缩伪影、模糊、振铃等"+"\n"+"Upscale将图像放大"+"\n"+"AutoDownscalePre用于将upscale放大的图像拉伸回屏幕"+"\n"+"Thin让线条变薄，Darken让线条变深"+"\n"+"同级效果与消耗性能UL>VL>L>M>S"+"\n"+"Soft版效果和性能消耗略低于非soft",bg='#9AC0CD',font=('宋体',15))
    help_frame_lable1.place(relx=0,rely=0.4,relheight=0.6,relwidth=1)



    #* 创建一个存放主要着色器的列表
    old_shaders_list = []
    pattern =r"Anime4K_\w+.glsl"
    Restore_result = re.findall(pattern,Anime4K_setting_List[anime4K_open])
    if len(Restore_result) != 0:
        for i in range(1,len(Restore_result)):
            old_shaders_list.append(Restore_result[i][0:len(Restore_result[i])-5])
    for i in range(len(old_shaders_list)):
        old_shaders_text.insert('insert',old_shaders_list[i]+"\n")

    #* 配置Anime4K着色器的函数
    def save_Anime4K_shaders(shaders_list):
        Anime4K_setting_List[anime4K_open] = "CTRL+1 no-osd change-list glsl-shaders set \"~~/shaders/Anime4K_Clamp_Highlights.glsl"
        i = 0
        for i in range(len(shaders_list)):
            Anime4K_setting_List[anime4K_open] = Anime4K_setting_List[anime4K_open] + ";~~/shaders/" + shaders_list[i] + ".glsl"
        Anime4K_setting_List[anime4K_open] = Anime4K_setting_List[anime4K_open] + "\"; show-text \"Anime4K已开启\""
        with open(Anime4K_setting_path,'w',encoding='utf-8') as test:
            for i in range(len(Anime4K_setting_List)):
                test.write(Anime4K_setting_List[i] +"\n")

    #* 设置保存部分
    def save_Anime4K_setting():
        save_Anime4K_shaders(new_shaders_list)
        msg = tkk.Label(top, text="已保存设置",bg='#87CEEB',font=('宋体',20))
        msg.place(relx=0.5,rely=0.5)

    save_Anime4K_setting_btn =tkk.Button(top,text='保存',command=save_Anime4K_setting)
    save_Anime4K_setting_btn.place(relx=0,rely=0.8,relheight=0.2,relwidth=0.25)

def MPV_setting_Command():
    path = os.getcwd()
    os.system("explorer " + str(path) + "\MPV\portable_config\mpv.conf")
    os.system("explorer " + str(path) + "\MPV\portable_config\Glow.exe")
    os.system("explorer " + str(path) + "\document\mpvhelp.txt")

def hele_Command():
    top = tkk.Toplevel()
    top.title("关于")
    width = 300
    height = 200
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height,(screenwidth-width)/2,(screenheight-height)/2)
    top.geometry(size_geo)
    top.attributes('-topmost',True)
    icon_path = os.getcwd() + "\document\\analysis.ico"
    top.iconbitmap(icon_path)
    msgl = tkk.Label(top,text="关于",bg='#87CEEB',font=('宋体',20))
    msgl.place(relx=0,rely=0,relheight=1,relwidth=0.3)
    msgr = tkk.Label(top,text="这个页面\n以后再更新了",font=('宋体',14))
    msgr.place(relx=0.4,rely=0,relheight=1,relwidth=0.5)

def Anime4K_hele_Command():
    path = os.getcwd()
    os.system("explorer " + str(path) + "\document\Anime4Khelp.txt") #* 通过cmd的explorer(资源管理器)打开文件

def tools_Command():
    top = tkk.Toplevel()
    top.title("格式化重命名工具")
    width = 400
    height = 260
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height,(screenwidth-width)/2,(screenheight-height)/2)
    top.geometry(size_geo)
    top.attributes('-topmost',True)
    icon_path = os.getcwd() + "\document\\analysis.ico"
    top.iconbitmap(icon_path)

    #* 创建输入框控件
    new_path_entry = tkk.Entry(top)
    #* 放置输入框，并设置位置
    new_path_entry.place(anchor="center",relx=0.6,rely=0.25,relwidth=0.5)
    new_path_entry.delete(0,"end")
    #* 设置当前输入框名字
    new_path_entry_name = tkk.Label(top,text='文件目录：',font=('宋体',14))
    new_path_entry_name.place(relx=0,rely=0.2,relwidth=0.3)

    new_name_entry = tkk.Entry(top)
    #* 放置输入框，并设置位置
    new_name_entry.place(anchor="center",relx=0.6,rely=0.45,relwidth=0.5)
    new_name_entry.delete(0,"end")
    new_name_entry_name = tkk.Label(top, text="新名称：",font=('宋体',14))
    new_name_entry_name.place(relx=0,rely=0.4,relwidth=0.3)

    new_offset_entry = tkk.Entry(top)
    #* 放置输入框，并设置位置
    new_offset_entry.place(anchor="center",relx=0.6,rely=0.65,relwidth=0.5)
    new_offset_entry.delete(0,"end")
    new_offset_entry_name = tkk.Label(top, text="偏移量：",font=('宋体',14))
    new_offset_entry_name.place(relx=0,rely=0.6,relwidth=0.3)

    def click_button():
        new_path = new_path_entry.get()
        new_path = "\"" + new_path + "\""
        new_name = new_name_entry.get()
        new_name = "\"" + new_name + "\""
        new_offset = new_offset_entry.get()
        Rename.main(new_path,new_name,new_offset)
    #* 点击按钮时执行的函数
    button = tkk.Button(top,text="确定",command=click_button)
    button.place(anchor="center",relx=0.5,rely=0.8,relwidth=0.2)

def check_updata_Command():
    path = os.getcwd() + "\\document\\setting.txt"
    with open(path,'r',encoding='utf-8') as ver:
        local_vre = ver.readline()                 #* 获取本地程序的版本
    local_vre = re.findall(r"\d+.\d+.\d+",local_vre)
    local_vre = local_vre[0]
    updata.main(local_vre)

def set_path_Command():
    path = os.getcwd() + "\\tools\\set.bat"
    os.system(path)

# 使窗口居中
def center():
    width = 800
    height = 600
    #* 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    window.geometry(size_geo)

if __name__ == "__main__":
    multiprocessing.freeze_support()                 #* 让打包程序识别这个是多进程文件
    #* 创建主窗口
    window = tkk.Tk()

    #* 设置主窗口背景颜色
    window.config(bg='#87CEEB')
    window.title("urlanalysis")
    center()
    icon_path = os.getcwd() + "\document\\analysis.ico"
    window.iconbitmap(icon_path)

    #* 创建一个主目录菜单，也被称为顶级菜单
    main_menu = tkk.Menu(window)

    #* 在顶级菜单上新增"设置"菜单的子菜单，同时不添加分割线
    setting_menu = tkk.Menu(main_menu, tearoff=False)
    #* 新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
    setting_menu.add_command(label="调整Anime4K着色器配置",command=Anime4K_setting_Command,accelerator="")
    setting_menu.add_command(label="调整MPV配置",command=MPV_setting_Command,accelerator="")

    help_menu = tkk.Menu(main_menu, tearoff=False)
    help_menu.add_command(label="Anime4K说明",command=Anime4K_hele_Command,accelerator="")
    #* 在help_menu字菜单中添加一条分割线
    help_menu.add_separator()
    help_menu.add_command(label="关于",command=hele_Command)

    tools_menu = tkk.Menu(main_menu, tearoff=False)
    tools_menu.add_command(label="格式化重命名工具",command=tools_Command)
    tools_menu.add_separator()
    tools_menu.add_command(label="设置环境变量",command=set_path_Command)
    tools_menu.add_command(label="检测更新",command=check_updata_Command)

    #* 在主目录菜单上新增"文件"选项作为父菜单，并通过menu参数与下拉菜单绑定
    main_menu.add_cascade(label="设置",menu=setting_menu)
    main_menu.add_cascade(label="帮助",menu=help_menu)
    main_menu.add_cascade(label="小工具",menu=tools_menu)

    #* 创建输入框控件
    ulr_entry = tkk.Entry(window)
    #* 放置输入框，并设置位置
    ulr_entry.place(anchor="center",relx=0.5,rely=0.4,relwidth=0.8)
    ulr_entry.delete(0, "end")

    #* 当按钮被点击的时候执行click_button()函数
    def click_button():
        ulr = ulr_entry.get()
        os.system("mpv \"" + str(ulr) +"\"")
        ulr_entry.delete(0,"end")
    #* 点击按钮时执行的函数
    button = tkk.Button(window,text="确定",command=click_button)
    button.place(anchor="center",relx=0.5,rely=0.6,relwidth=0.2)

    #* 显示菜单
    window.config(menu=main_menu)
    window.mainloop()


