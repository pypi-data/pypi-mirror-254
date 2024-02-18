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
from xtkinter.widgets.xtk_sizegrip import XtkSizegrip
from xtkinter.widgets.xtk_frame import topTitleFrame
from xtkinter.widgets.xtk_frame import GraphicalRoundedFrame, CanvasRoundedFrame

from PIL import Image, ImageTk

LIB_PATH = site.getsitepackages()[1]

class XtkToplevel(tk.Toplevel):
    def __init__(self, isscale:bool=False, shutdown=None, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.isscale = isscale
        if self.isscale == True:
            self.scale_width_list, self.scale_height_list = [100, 100], [100, 100]  # [初始值, 当前值]  用于记录窗口缩放时的宽高
            self._widgets = []  # 子部件列表
            self.bind('<Configure>', self._scale)  # 开启窗口缩放检测

    def _scale(self, event) -> None:
        """ 缩放检测 """
        width, height = map(int, self.geometry().split('+')[0].split('x'))
        # NOTE: 此处必须用 geometry 方法，直接用 Event 会有画面异常的 bug

        if (width, height) == (self.scale_width_list[1], self.scale_height_list[1]):  # 没有大小的改变
            return

        for widgets in self._widgets:
            if not widgets.expand:  # 部件是否支持缩放
                continue
            widgets.scale(width/self.width[1], height/self.height[1])

        # 更新窗口当前的宽高值
        self.scale_width_list[1], self.scale_height_list[1] = width, height

    @property
    def widgets(self) -> tuple:
        """ 获取窗口下的一级组件的元组 """

    @widgets.getter
    def widgets(self) -> tuple:
        return tuple(self._widgets)

class CornerWindow(XtkToplevel):
    def __init__(self,
                 icon: str = None,
                 title: str = '自定义方形窗口',
                 title_height: int = 28,
                 inner_bd: int = 2,
                 win_width:int = 300,
                 win_height:int = 300,
                 win_outline_color:str = '#fff000',
                 win_outline_width:int = 2,
                 title_frame_bg: str = None,
                 main_frame_bg:str = None,
                 *args, **kwargs):
        XtkToplevel.__init__(self, *args, **kwargs)  # 功能同上
        if icon == None:
            self.title_icon = LIB_PATH + '/xtkinter/assets/icon/favicon.ico'
        else:
            self.title_icon = icon
        self.title_text = title
        self.title_frame_bg = title_frame_bg
        self.main_frame_bg = main_frame_bg
        self.win_width = win_width
        self.win_height = win_height
        self.geometry(f'{self.win_width}x{self.win_height}+100+100')
        if self.isscale == True:
            self.scale_width_list = [self.win_width, self.win_width]
            self.scale_height_list = [self.win_height, self.win_height]
        self.overrideredirect(True)
        self['highlightthickness'] = win_outline_width
        self['highlightcolor'] = win_outline_color
        self['relief'] = 'flat'
        self.window = tk.Frame(self, background=self.title_frame_bg)
        self.window.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.title_frame = topTitleFrame(self.window, title_text=self.title_text, title_icon=self.title_icon,
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
        g = f'{self.win_width}x{self.win_height}+{newX}+{newY}'
        self.geometry(g)

    # 鼠标左键抬起时的事件处理函数
    def onLeftButtonUp(self, event):
        self.canMove.set(0)
        if event.widget == self.title_frame.close_btn:
            self.destroy()

    # 鼠标右键抬起时的事件处理函数(关闭事件)
    def onRightButtonUp(self, event):
        self.destroy()

class CanvasRoundedWindow(XtkToplevel):
    def __init__(self,
                 icon: str = None,
                 title: str = '绘制自定义圆角窗口',
                 title_height: int = 28,
                 title_frame_bg:str = None,
                 inner_bd: int = 2,
                 win_width:int = 300,
                 win_height:int = 300,
                 win_transparent_color: str = None,  # '#343B61' 此处的透明色一定要设一个与背影色相近的色值，并在之后从不使用此值给任何小部件
                 win_bg: str = None,
                 win_outline_color: str = None,
                 win_outline_width: int =2,
                 main_frame_bg:str = '#ffffff',
                 radii:int = 10,
                 *args, **kwargs):  # '#343B48' 窗体的背景色
        XtkToplevel.__init__(self, *args, **kwargs)  # 功能同上
        if icon == None:
            self.title_icon = LIB_PATH + '/xtkinter/assets/icon/favicon.ico'
        else:
            self.title_icon = icon
        self.title_text = title
        self.title_frame_bg = title_frame_bg
        self.win_transparent_color = win_transparent_color
        self.win_bg = win_bg
        self.win_outline_color = win_outline_color
        self.win_outline_width = win_outline_width
        self.win_width = win_width
        self.win_height = win_height
        self.radii = radii
        self.geometry(f'{self.win_width}x{self.win_height}+100+100')
        if self.isscale == True:
            self.scale_width_list = [self.win_width, self.win_width]
            self.scale_height_list = [self.win_height, self.win_height]
        self.overrideredirect(True)
        self.minsize(self.win_width, self.win_height)
        if self.win_transparent_color is None:
            raise ValueError(f"transparent_color is None, 如果想做圆角模式请为transparent_color赋值")
        # 设置某个色值为透明色，这样图片中所有该色区域都被认为是透明的了
        self.wm_attributes('-transparentcolor',
                           self.win_transparent_color)  # 此处用的color是与要使用的色值相似的值，比如如果使用 #ec4141,则color就设为#ec4142
        self.window = CanvasRoundedFrame(self, frame_width=self.win_width, frame_height=self.win_height, root_bg_color=self.win_transparent_color,
                                               frame_bg=self.win_bg, frame_outline_color=self.win_outline_color,
                                               frame_outline_width=self.win_outline_width, radii=self.radii)
        self.window.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_frame = topTitleFrame(self.window, title_icon=self.title_icon, title_text=self.title_text,
                                      title_bg=self.title_frame_bg,
                                      title_width=self.win_width - self.radii, title_height=title_height,
                                      inner_bd=inner_bd)
        self.title_frame.place(x=self.radii / 2, y=self.win_outline_width + 2, width=self.win_width - self.radii,
                               height=title_height)
        self.main_frame = tk.Frame(self.window, background=main_frame_bg)
        self.main_frame.place(x=2 * inner_bd, y=title_height + 2 * inner_bd, width=self.win_width - 4 * inner_bd,
                              height=self.win_height - title_height - 4 * inner_bd)

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
        g = f'{self.win_width}x{self.win_height}+{newX}+{newY}'
        self.geometry(g)

    # 鼠标左键抬起时的事件处理函数
    def onLeftButtonUp(self, event):
        self.canMove.set(0)
        if event.widget == self.title_frame.close_btn:
            self.destroy()

    # 鼠标右键抬起时的事件处理函数(关闭事件)

    def onRightButtonUp(self, event):
        self.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x450+100+100')

    def create_new_window():
        # new_window = GraphicalRoundedWindow(xtk_width=300, xtk_height=200, transparent_color='#343B61', title_frame_bg='#343B48', radii=85, isdebug=False)
        new_window = CornerWindow(xtk_width=300, xtk_height=200, title_frame_bg='#343B48',main_frame_bg='#ffffff')
        # new_window = CanvasRoundedWindow(xtk_width=300, xtk_height=200, transparent_color='#343B61', window_bg='#343B48', window_outline_color='#ffffff', window_outline_width=3, radii=10)


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