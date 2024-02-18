# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import time
import tkinter as tk
from tkinter import ttk
from xtkinter.windows import xtk_tk as xtk
from xtkinter.xtkthemes.xtk_themes import ThemedStyle

from math import cos, pi, sin, sqrt  # 实现缩放功能及移动函数功能

from PIL import Image, ImageTk

def move(master, widget,
    dx: int,
    dy: int,
    times: int,
    mode,
    frames: int = 30,
    **kw
) -> None:
    """
    ### 移动函数
    以特定方式移动由 Place 布局的某个控件或某些控件的集合或图像\n
    `master`: 控件所在的父控件
    `widget`: 要移动位置的控件
    `dx`: 横向移动的距离（单位：像素）
    `dy`: 纵向移动的距离（单位：像素）
    `times`: 移动总时长（单位：毫秒）
    `mode`: 移动速度模式，为 smooth（顺滑）、rebound（回弹）和 flat（平移）这三种，或者为元组 (函数, 起始值, 终止值) 的形式
    `frames`: 帧数，越大移动就越流畅，但计算越慢（范围为 1~100）
    """
    if kw.get('_ind'):  # 记忆值
        displacement = mode
    elif mode == 'flat':  # 平滑模式
        displacement = (100/frames,) * frames
    elif mode == 'smooth':  # 流畅模式
        return move(master, widget, dx, dy, times, (sin, 0, pi), frames)
    elif mode == 'rebound':  # 回弹模式
        return move(master, widget, dx, dy, times, (cos, 0, 0.6*pi), frames)
    else:  # 函数模式
        func, start, end = mode
        interval = (end-start) / frames
        displacement = [func(start+interval*i) for i in range(1, frames+1)]
        key = 100 / sum(displacement)
        displacement = [key*i for i in displacement]

    if kw.get('_ind'):
        if isinstance(displacement, tuple):
            displacement = list(displacement)

        displacement[kw['_ind']] += displacement[kw['_ind']-1]

    proportion = displacement[kw.get('_ind', 0)] / 100  # 总计实际应该移动的百分比
    x = round(proportion * dx - kw.get('_x', 0))  # 此次横向移动量
    y = round(proportion * dy - kw.get('_y', 0))  # 此次纵向移动量

    if isinstance(master, tk.Misc) and isinstance(widget, tk.BaseWidget):  # tkinter 的控件
        place_info = widget.place_info()
        origin_x, origin_y = int(place_info['x']), int(place_info['y'])
        widget.place(x=origin_x+x, y=origin_y+y)
    elif isinstance(widget, tk.Tk) or isinstance(widget, tk.Toplevel):
        geometry, ox, oy = widget.geometry().split('+')
        widget.geometry('%s+%d+%d' % (geometry, int(ox)+x, int(oy)+y))
    else:
        widget.move(x, y)
    if kw.get('_ind', 0)+1 == frames:  # 停止条件
        return
    args =master, widget, dx, dy, times, displacement, frames
    kw = {'_x': kw.get('_x', 0) + x,
          '_y': kw.get('_y', 0) + y,
          '_ind': kw.get('_ind', 0) + 1}
    master.after(round(times/frames), lambda: move(*args, **kw))  # 间隔一定时间执行函数

class titleSettingBtn:
    def __init__(self, title_frame, bind_widget,
                 icon:str,
                 title_frame_bg,):
        self.title_frame = title_frame
        self.bind_widget = bind_widget
        self.icon = icon
        self.title_frame_bg = title_frame_bg
        self.issetting = False
        icon_image = Image.open(self.icon)
        self.photo = ImageTk.PhotoImage(icon_image)
        title_frame.update()
        title_setting_btn = tk.Label(self.title_frame, image=self.photo, bg=self.title_frame_bg)
        title_setting_btn.place(x=self.title_frame.winfo_width() - 105, y=4, width=30, height=24)

        title_setting_btn.bind("<Enter>", self.on_enter)
        title_setting_btn.bind("<Leave>", self.on_leave)
        title_setting_btn.bind('<ButtonRelease-1>', self.on_leftClick)

    def on_enter(self, enevt):
        enevt.widget.configure(bg='#ec4141')

    def on_leave(self, enevt):
        enevt.widget.configure(bg=self.title_frame_bg)

    def on_leftClick(self, enevt):
        if self.issetting == False:
            move(self.bind_widget.master, self.bind_widget, -self.bind_widget.winfo_width(), 0, 300, mode='rebound')
            self.issetting = True
        else:
            move(self.bind_widget.master, self.bind_widget, self.bind_widget.winfo_width(), 0, 300, mode='rebound')
            self.issetting = False

class editThemeFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['bg'] = self.master['bg']
        style = ThemedStyle()
        style.set_theme('arc')
        theme_selection = ttk.Frame(self, padding=(10, 10, 10, 10))
        # theme_selection.pack(fill=tk.X, expand=tk.YES)
        theme_selection.place(x=0, y=0, relwidth=1, height=40)
        lbl = ttk.Label(theme_selection, text="修改主题")
        lbl.pack(side=tk.LEFT)

    def save(self):
        print('edit保存完成')

class newThemeFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['bg'] = self.master['bg']
        theme_selection = ttk.Frame(self, padding=(10, 10, 10, 10))
        theme_selection.place(x=0, y=0, relwidth=1, height=40)
        lbl = ttk.Label(theme_selection, text="新建主题")
        lbl.pack(side=tk.TOP)

    def save(self):
        print('new保存完成')

class leftMenu(tk.Frame):
    def __init__(self, master, bind_frame,
                 btn_width:int,
                 btn_height:int,
                 btn_bg:str,
                 btn_fg:str,
                 enter_bg:str,
                 press_bg:str,
                 decorate_bar_bg:str,
                 btn_icon: str = None,
                 btn_text: str = None,
                 *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.bind_frame = bind_frame
        self.bind_frame_top = None
        self.btn_width = btn_width
        self.btn_height = btn_height
        self.btn_bg = btn_bg
        self.btn_fg = btn_fg
        self.enter_bg = enter_bg
        self.press_bg = press_bg
        self.decorate_bar_bg = decorate_bar_bg
        self['bg'] = self.btn_bg
        self.ishide = False
        self.menuBtns:list[menuBtn] = []

        self.hide_menuBtn = menuBtn(self, is_page=False, btn_width=self.btn_width, btn_height=self.btn_height, btn_bg=self.btn_bg, btn_fg=self.btn_fg,
                               decorate_bar_bg=self.decorate_bar_bg, enter_bg=self.enter_bg, press_bg=self.press_bg, btn_icon='./assets/icon/icon_menu.png',
                               btn_text=' 隐 藏')
        self.hide_menuBtn.place(x=0, y=20, width=129, height=40)

        self.edit_menuBtn = menuBtn(self, is_page=True, btn_width=self.btn_width, btn_height=self.btn_height, btn_bg=self.btn_bg, btn_fg=self.btn_fg,
                               decorate_bar_bg=self.decorate_bar_bg, enter_bg=self.enter_bg, press_bg=self.press_bg, btn_icon='./assets/icon/cil-gamepad.png',
                               btn_text='修改主题')
        self.edit_menuBtn.place(x=0, y=80, width=129, height=40)
        self.edit_themeFrame = editThemeFrame(self.bind_frame)
        self.edit_themeFrame.place(x=0, y=0, relwidth=1, relheight=1)
        self.edit_themeFrame.lower()
        for value in self.menuBtns:
            if value[0] == self.edit_menuBtn:
                value[3] = self.edit_themeFrame

        self.new_menuBtn = menuBtn(self, is_page=True,  btn_width=self.btn_width, btn_height=self.btn_height, btn_bg=self.btn_bg,
                                   btn_fg=self.btn_fg,
                                   decorate_bar_bg=self.decorate_bar_bg, enter_bg=self.enter_bg, press_bg=self.press_bg,
                                   btn_icon='./assets/icon/cil-file.png',
                                   btn_text='新建主题')
        self.new_menuBtn.place(x=0, y=140, width=129, height=40)
        self.new_themeFrame = newThemeFrame(self.bind_frame)
        self.new_themeFrame.place(x=0, y=0, relwidth=1, relheight=1)
        self.new_themeFrame.lower()
        for value in self.menuBtns:
            if value[0] == self.new_menuBtn:
                value[3] = self.new_themeFrame

        self.save_menuBtn = menuBtn(self, is_page=False, btn_width=self.btn_width, btn_height=self.btn_height, btn_bg=self.btn_bg,
                                   btn_fg=self.btn_fg,
                                   decorate_bar_bg=self.decorate_bar_bg, enter_bg=self.enter_bg, press_bg=self.press_bg,
                                   btn_icon='./assets/icon/cil-save.png',
                                   btn_text=' 保 存')
        self.save_menuBtn.place(x=0, y=200, width=129, height=40)

        self.hide_menuBtn.btn_icon_label.bind('<ButtonRelease-1>', self.hide_clickEvent)
        self.hide_menuBtn.btn_text_label.bind('<ButtonRelease-1>', self.hide_clickEvent)

        self.edit_menuBtn.btn_icon_label.bind('<ButtonRelease-1>', self.edit_clickEvent)
        self.edit_menuBtn.btn_text_label.bind('<ButtonRelease-1>', self.edit_clickEvent)
        self.new_menuBtn.btn_icon_label.bind('<ButtonRelease-1>', self.new_clickEvent)
        self.new_menuBtn.btn_text_label.bind('<ButtonRelease-1>', self.new_clickEvent)
        self.save_menuBtn.btn_icon_label.bind('<ButtonRelease-1>', self.save_clickEvent)
        self.save_menuBtn.btn_text_label.bind('<ButtonRelease-1>', self.save_clickEvent)

    def hide_clickEvent(self, enevt):
        self.hide_menuBtn.on_leftBtnUp(enevt)
        width_off = self.bind_frame.winfo_width() + (self.btn_width - 60)
        width_on = self.bind_frame.winfo_width() - (self.btn_width - 60)
        if self.ishide == False:
            # self.bind_frame.place(width=width_off)
            self.bind_frame.place(x=60, y=0, width=width_off, relheight=1)
            # move(self.bind_frame.master, self.bind_frame, -(self.btn_width - 60), 0, 100, mode='smooth')
            self.ishide = True
        else:
            # self.bind_frame.place(width=width_on)
            self.bind_frame.place(x=129, y=0, width=width_on, relheight=1)
            # move(self.bind_frame.master, self.bind_frame, (self.btn_width - 60), 0, 100, mode='smooth')
            self.ishide = False

    def edit_clickEvent(self, enevt):
        self.edit_menuBtn.on_leftBtnUp(enevt)
        self.edit_themeFrame.lift()
        self.bind_frame_top = self.edit_themeFrame

    def new_clickEvent(self, enevt):
        self.new_menuBtn.on_leftBtnUp(enevt)
        self.new_themeFrame.lift()
        self.bind_frame_top = self.new_themeFrame

    def save_clickEvent(self, enevt):
        # move(self.bind_frame.master, self.bind_frame, -(self.btn_width - 60), 0, 300, mode='rebound')
        self.save_menuBtn.on_leftBtnUp(enevt)
        for value in self.menuBtns:
            if value[1] == 1:
                current_frame = value[3]
                current_frame.save()

class menuBtn(tk.Frame):
    def __init__(self, master,
                 is_page:bool,
                 btn_width: int,
                 btn_height: int,
                 btn_bg: str,
                 btn_fg: str,
                 enter_bg: str,
                 press_bg: str,
                 decorate_bar_bg: str,
                 btn_icon: str = None,
                 btn_text: str = None,
                 *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.is_page = is_page
        self.btn_icon = btn_icon
        self.btn_text = btn_text
        self.btn_width = btn_width
        self.btn_height = btn_height
        self.btn_bg = btn_bg
        self.btn_fg = btn_fg
        self.enter_bg = enter_bg
        self.press_bg = press_bg
        self.decorate_bar_bg = decorate_bar_bg
        self['bg'] = self.btn_bg
        self.decorate_bar = tk.Label(self, bg=self.btn_bg)
        self.decorate_bar.place(x=0, y=0, width=5, relheight=1)
        icon_image = Image.open(self.btn_icon)
        self.photo = ImageTk.PhotoImage(icon_image)
        self.btn_icon_label = tk.Label(self, image=self.photo, bg=self.btn_bg)
        self.btn_icon_label.place(x=5, y=0, width=50, height=40)
        self.btn_text_label = tk.Label(self, text=self.btn_text, bg=self.btn_bg, fg=self.btn_fg)
        self.btn_text_label.place(x=55, y=0, width=self.btn_width-55, relheight=1)

        self.master.menuBtns.append([self, 0, self.is_page, None])

        self.btn_icon_label.bind("<Enter>", self.on_enter)
        self.btn_text_label.bind("<Enter>", self.on_enter)
        self.btn_icon_label.bind("<Leave>", self.on_leave)
        self.btn_text_label.bind("<Leave>", self.on_leave)
        self.btn_icon_label.bind('<Button-1>', self.on_leftBtnDown)
        self.btn_text_label.bind('<Button-1>', self.on_leftBtnDown)
        self.btn_icon_label.bind('<ButtonRelease-1>', self.on_leftBtnUp)
        self.btn_text_label.bind('<ButtonRelease-1>', self.on_leftBtnUp)


    def on_enter(self, enevt):
        i = 0
        for value in self.master.menuBtns:
            if enevt.widget.master == value[0] and value[1] == 0:
                self['bg'] = self.enter_bg
                self.decorate_bar.configure(bg=self.enter_bg)
                self.btn_icon_label.configure(bg=self.enter_bg)
                self.btn_text_label.configure(bg=self.enter_bg)
            i += 1

    def on_leave(self, enevt):
        i = 0
        for value in self.master.menuBtns:
            if enevt.widget.master == value[0] and value[1] == 1:
                self['bg'] = self.enter_bg
                self.decorate_bar.configure(bg=self.decorate_bar_bg)
                self.btn_icon_label.configure(bg=self.enter_bg)
                self.btn_text_label.configure(bg=self.enter_bg)
            if value[1] == 0:
                self.master.menuBtns[i][0]['bg'] = self.btn_bg
                self.master.menuBtns[i][0].decorate_bar.configure(bg=self.btn_bg)
                self.master.menuBtns[i][0].btn_icon_label.configure(bg=self.btn_bg)
                self.master.menuBtns[i][0].btn_text_label.configure(bg=self.btn_bg)
            i += 1

    def on_leftBtnDown(self, enevt):
        i = 0
        for value in self.master.menuBtns:
            if enevt.widget.master == value[0] and value[1] == 0:
                self['bg'] = self.press_bg
                self.decorate_bar.configure(bg=self.press_bg)
                self.btn_icon_label.configure(bg=self.press_bg)
                self.btn_text_label.configure(bg=self.press_bg)
            i += 1

    def on_leftBtnUp(self, enevt):
        if self.is_page == True:
            self['bg'] = self.enter_bg
            self.decorate_bar.configure(bg=self.decorate_bar_bg)
            self.btn_icon_label.configure(bg=self.enter_bg)
            self.btn_text_label.configure(bg=self.enter_bg)
            i = 0
            for value in self.master.menuBtns:
                if enevt.widget.master == value[0]:
                    self.master.menuBtns[i][1] = 1
                else:
                    self.master.menuBtns[i][1] = 0

                if value[1] == 0:
                    self.master.menuBtns[i][0]['bg'] = self.btn_bg
                    self.master.menuBtns[i][0].decorate_bar.configure(bg=self.btn_bg)
                    self.master.menuBtns[i][0].btn_icon_label.configure(bg=self.btn_bg)
                    self.master.menuBtns[i][0].btn_text_label.configure(bg=self.btn_bg)
                i += 1
        else:
            self['bg'] = self.btn_bg
            self.decorate_bar.configure(bg=self.btn_bg)
            self.btn_icon_label.configure(bg=self.btn_bg)
            self.btn_text_label.configure(bg=self.btn_bg)


if __name__ == '__main__':
    xtk_width = 1200
    xtk_height = 700
    title_height = 30
    title_bg = '#21252b'
    win_bg = '#21252b'
    win_transparent_color = '#212525'
    inner_bd = 4
    # root = xtk.CornerWindow(win_width=xtk_width, win_height=xtk_height, win_outline_color='#BBB', win_outline_width=2, title_frame_bg='#343B48')
    # root = xtk.GraphicalRoundedWindow(win_width=xtk_width, win_height=xtk_height, win_transparent_color='#212525', win_bg='#21252b',
    #                                   title_frame_bg='#343B48')
    root = xtk.CanvasRoundedWindow(win_width=xtk_width, win_height=xtk_height, title='滑动测试案例', title_height=title_height, title_frame_bg=title_bg,
                                   inner_bd=inner_bd, win_transparent_color=win_transparent_color, win_bg=win_bg, win_outline_color='#BBB',
                                   win_outline_width=2, radii=10)
    style = ThemedStyle()
    style.set_theme('xttk')
    # print(style.theme_names())
    # print(style.theme_use())

    left_frame = tk.Frame(root.main_frame, background='#21252b')
    left_frame.place(x=0, y=0, width=129, relheight=1)

    middle_frame = tk.Frame(root.main_frame, background='#282c34')  # 282c34
    middle_frame.place(x=129, y=0, width=xtk_width - 2 * inner_bd - 129, relheight=1)
    middle_frame_masking_out = tk.Frame(middle_frame, background='#282c34')
    middle_frame_masking_out.place(x=0, y=0, relwidth=1, relheight=1)
    label_image = Image.open('./assets/image/PyXTk.png')
    label_image = ImageTk.PhotoImage(label_image)
    middle_label = tk.Label(middle_frame_masking_out, bg='#282c34', image=label_image)
    middle_label.pack(expand=True, fill='both')

    right_frame = tk.Frame(root.main_frame, background='#fff000')  # 21252b
    right_frame.place(x=xtk_width, y=0, width=300, relheight=1)

    left_menu = leftMenu(left_frame, middle_frame, btn_width=129, btn_height=40, btn_bg='#21252b', btn_fg='#fff',
                         decorate_bar_bg='#ff79c6',
                         enter_bg='#282c34', press_bg='#bd93f9')
    left_menu.place(x=0, y=0, relwidth=1, relheight=1)
    title_setting_btn = titleSettingBtn(root.title_frame, right_frame, icon='./assets/icon/cil-settings.png', title_frame_bg=title_bg)

    root.mainloop()