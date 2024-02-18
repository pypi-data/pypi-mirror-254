# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import os
import sys
import site
import tkinter as tk
from tkinter import ttk
from ctypes import OleDLL
from typing import Union
from xtkinter.windows import xtk_tk
from xtkinter.widgets.xtk_frame import topTitleFrame
from xtkinter.widgets.xtk_frame import InnerWindowRoundedFrame

from PIL import Image, ImageTk

LIB_PATH = site.getsitepackages()[1]

class CornerInnerWindow(tk.Frame):
    def __init__(self,master,
                 icon: str = None,
                 title: str = '自定义方形内窗口',
                 title_height: int = 28,
                 inner_bd: int = 2,
                 win_width:int = 300,
                 win_height:int = 300,
                 win_outline_color:str = '#ffffff',
                 win_outline_width:int = 2,
                 title_frame_bg: str = None,
                 main_frame_bg:str = None,
                 isscale = False,
                 *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)  # 功能同上
        self.master = master
        if icon == None:
            self.title_icon = LIB_PATH + '/xtkinter/assets/icon/favicon.ico'
        else:
            self.title_icon = icon
        self['background'] = title_frame_bg
        self.title_text = title
        self.title_frame_bg = title_frame_bg
        self.main_frame_bg = main_frame_bg
        self.win_width = win_width
        self.win_height = win_height
        self.inner_bd = inner_bd
        self.isscale = isscale  # 暂未实现缩放功能
        self.place(x=100, y=100, width=self.win_width, height=self.win_height)
        self['highlightthickness'] = win_outline_width
        self['highlightcolor'] = win_outline_color
        self['relief'] = 'flat'
        self.title_frame = topTitleFrame(self, title_text=self.title_text, title_icon=self.title_icon,
                                         title_bg=self.title_frame_bg, title_width=self.win_width,
                                         title_height=title_height, inner_bd=inner_bd)
        self.title_frame.place(x=0, y=0, relwidth=1, height=title_height)

        self.main_frame = tk.Frame(self, background=main_frame_bg)
        self.main_frame.place(x=inner_bd, y=title_height + inner_bd, width=self.win_width - 4 * inner_bd,
                              height=self.win_height - title_height - 4 * inner_bd)

        # 鼠标左键按下时设置为1表示可移动窗口，抬起后不可移动
        self.canMove = tk.IntVar(self, value=0)
        # 记录鼠标左键按下的位置
        self.X = tk.IntVar(self, value=0)
        self.Y = tk.IntVar(self, value=0)
        self.title_frame.bind('<Button-1>', self.onLeftButtonDown)
        self.title_frame.bind('<B1-Motion>', self.onLeftButtonMove)
        self.title_frame.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        self.title_frame.title_text.bind('<Button-1>', self.onLeftButtonDown)
        self.title_frame.title_text.bind('<B1-Motion>', self.onLeftButtonMove)
        self.title_frame.title_text.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        # self.title_frame.bind('<ButtonRelease-3>', self.onRightButtonUp)
        self.title_frame.close_btn.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        self.main_frame.bind('<ButtonRelease-1>', self.onLeftButtonUp)

    def scale(self):
        # 暂未实现缩放功能
        pass

    # 鼠标左键按下时的事件处理函数
    def onLeftButtonDown(self, event):
        self.X.set(event.x)
        self.Y.set(event.y)
        self.canMove.set(1)

    # 鼠标移动时的事件处理函数
    def onLeftButtonMove(self, event):
        if self.canMove.get() == 0:
            return
        newX = self.winfo_x() + (event.x - self.X.get())
        newY = self.winfo_y() + (event.y - self.Y.get())
        if newX < 0:
            newX = 0
        if newX > self.master.winfo_width()- self.win_width:
            newX = self.master.winfo_width()- self.win_width
        if newY < 0:
            newY = 0
        if newY > self.master.winfo_height() - self.win_height:
            newY = self.master.winfo_height() - self.win_height
        self.place(x=newX, y=newY, width=self.win_width, height=self.win_height)

    # 鼠标左键抬起时的事件处理函数
    def onLeftButtonUp(self, event):
        self.canMove.set(0)
        if event.widget == self.title_frame.close_btn:
            self.destroy()
            return
        self.lift()     # 让对象置前

    # 鼠标右键抬起时的事件处理函数(关闭事件)
    def onRightButtonUp(self, event):
        self.destroy()

class CanvasRoundedInnerWindow(tk.Frame):
    def __init__(self,master,
                 icon: str = None,
                 title: str = '绘制自定义圆角内窗口',
                 title_height: int = 28,
                 title_frame_bg:str = None,
                 inner_bd: int = 2,
                 win_width:int = 300,
                 win_height:int = 300,
                 win_bg: str = None,
                 win_outline_color: str = None,
                 win_outline_width: int =2,
                 main_frame_bg:str = '#ffffff',
                 radii:int = 10,
                 isscale: bool = False,
                 *args, **kwargs):  # '#343B48' 窗体的背景色
        tk.Frame.__init__(self, *args, **kwargs)  # 功能同上
        self.root = master
        if icon == None:
            self.title_icon = LIB_PATH + '/xtkinter/assets/icon/favicon.ico'
        else:
            self.title_icon = icon
        self.title_text = title
        self.title_frame_bg = title_frame_bg
        self.isscale = isscale
        self['background'] = self.root['background']    # 内窗口基础框架的背景
        self.win_bg = win_bg
        self.win_outline_color = win_outline_color
        self.win_outline_width = win_outline_width
        self.win_width = win_width
        self.win_height = win_height
        self.radii = radii
        self.place(x=100, y=100, width=self.win_width, height=self.win_height)
        if self.isscale == True:
            self.scale_width_list = [self.win_width, self.win_width]
            self.scale_height_list = [self.win_height, self.win_height]

        self.window = InnerWindowRoundedFrame(self, rounded_width=self.win_width, rounded_height=self.win_height, rounded_bg=self.win_bg,
                                              rounded_outline_color=self.win_outline_color,
                                               rounded_outline_width=self.win_outline_width, radii=self.radii)
        self.window.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_frame = topTitleFrame(self.window, title_icon=self.title_icon, title_text=self.title_text,
                                      title_bg=self.title_frame_bg, title_width=self.win_width - self.radii, title_height=title_height,
                                      inner_bd=inner_bd)
        self.title_frame.place(x=self.radii / 2, y=self.win_outline_width + 2, width=self.win_width - self.radii,
                               height=title_height)
        self.main_frame = tk.Frame(self.window, background=main_frame_bg)
        self.main_frame.place(x=2*inner_bd, y=title_height + 2*inner_bd, width=self.win_width - 4*inner_bd,
                              height=self.win_height - title_height - 4*inner_bd)

        # self.si = XtkSizegrip(self, bg=self.window_bg)  # 创建一个Sizegrip组件
        # si.pack(side=tk.BOTTOM, anchor=tk.SE)  # 这种组件一般是位于窗体右下角
        # self.si.place(x=self.xtk_width-21, y=self.xtk_height - 21)

        # 鼠标左键按下时设置为1表示可移动窗口，抬起后不可移动
        self.canMove = tk.IntVar(self, value=0)
        # 记录鼠标左键按下的位置
        self.X = tk.IntVar(self, value=0)
        self.Y = tk.IntVar(self, value=0)
        self.title_frame.bind('<Button-1>', self.onLeftButtonDown)
        self.title_frame.bind('<B1-Motion>', self.onLeftButtonMove)
        self.title_frame.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        self.title_frame.title_text.bind('<Button-1>', self.onLeftButtonDown)
        self.title_frame.title_text.bind('<B1-Motion>', self.onLeftButtonMove)
        self.title_frame.title_text.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        # self.title_frame.bind('<ButtonRelease-3>', self.onRightButtonUp)
        self.title_frame.close_btn.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        # self.main_frame.bind('<ButtonRelease-1>', self.onLeftButtonUp)

    # 鼠标左键按下时的事件处理函数
    def onLeftButtonDown(self, event):
        self.X.set(event.x)
        self.Y.set(event.y)
        self.canMove.set(1)

    # 鼠标移动时的事件处理函数
    def onLeftButtonMove(self, event):
        if self.canMove.get() == 0:
            return
        newX = self.winfo_x() + (event.x - self.X.get())
        newY = self.winfo_y() + (event.y - self.Y.get())
        if newX < self.root.winfo_x():
            newX = self.root.winfo_x()
        if newX > self.root.winfo_width()- self.win_width + 2*self.win_outline_width:
            newX = self.root.winfo_width()- self.win_width + 2*self.win_outline_width
        if newY < self.root.winfo_y():
            newY = self.root.winfo_y()
        if newY > self.root.winfo_height() - self.win_height + self.title_frame.winfo_height() + 3*self.win_outline_width:
            newY = self.root.winfo_height() - self.win_height + self.title_frame.winfo_height() + 3*self.win_outline_width
        self.place(x=newX, y=newY, width=self.win_width, height=self.win_height)


    # 鼠标左键抬起时的事件处理函数
    def onLeftButtonUp(self, event):
        self.canMove.set(0)
        if event.widget == self.title_frame.close_btn:
            self.destroy()
            return
        self.lift()  # 让对象置前

    # 鼠标右键抬起时的事件处理函数(关闭事件)

    def onRightButtonUp(self, event):
        self.destroy()

if __name__ == '__main__':
    ico_path = '../assets/icon/favicon.ico'
    root = xtk_tk.CanvasRoundedWindow(xtk_width=800, xtk_height=450, transparent_color='#343B61', window_bg='#343B48', window_outline_color='#ffffff',
                                      window_outline_width=3, radii=10, icon=ico_path)
    # root.geometry('800x450+100+100')
    # root_bg_color = root['background']
    def create_new_window():
        new_window = CornerInnerWindow(root, frame_width=300, frame_height=200, title_frame_bg='#343B48', main_frame_bg='#ffffff')
        # new_window = CanvasRoundedWindow(root, frame_width=300, frame_height=200, root_bg_color=root_bg_color, frame_bg='#343B48',
        #                                  frame_outline_color='#ffffff', frame_outline_width=3, radii=10)
        print(root._widgets)

    button = tk.Button(root, text="打开新窗口", command=create_new_window)
    button.pack()
    # root = CornerWindow(xtk_width=800, xtk_height=600, title_frame_bg='#343B48',main_frame_bg='#ffffff')
    # root = GraphicalRoundedWindow(xtk_width=800, xtk_height=450, transparent_color='#343B61', title_frame_bg='#343B48', radii=85, isdebug=True)
    # root = CanvasRoundedWindow(xtk_width=800, xtk_height=450, transparent_color='#343B61', window_bg='#343B48', window_outline_color='#ffffff', window_outline_width=3, radii=10)
    # close_frame = tk.Frame(root.title_frame, background='#ec4141')
    # close_frame.place(x=0, y=0, width=20, relheight=1)
    # root.title_frame['background'] = '#343B48'
    # root.title_frame.place(x=12, width=976, height=30)
    # main_frame = tk.Frame(root.windows_frame, background='#fffff0')
    # main_frame.place(x=2, y=32, width=1000-4, height=800-52)
    # statusbar_frame = tk.Frame(root.windows_frame, background='#343B48')
    # statusbar_frame.place(x=12, y=750+30, width=1000-24, height=18)
    # view_frame = tk.Frame(root.main_frame, background='#fff000')
    # view_frame.place(relx=0, rely=0, width=300, height=300)
    root.mainloop()