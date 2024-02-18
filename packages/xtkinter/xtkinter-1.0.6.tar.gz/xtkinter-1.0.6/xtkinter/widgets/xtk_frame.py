# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import os
import site
import tkinter as tk
from xtkinter.utility.utility_func import rounded_rect

from PIL import Image, ImageTk, ImageDraw

LIB_PATH = site.getsitepackages()[1]

class XtkFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)

class GraphicalRoundedFrame(XtkFrame):
    def __init__(self, master,
                 rounded_width: int = 300,
                 rounded_height: int = 300,
                 win_transparent_color: str = None,  # '#343B61' 此处的透明色一定要设一个与frame_bg相近的色值，并在之后从不使用此值给任何小部件
                 rounded_bg:str = None,
                 image_name:str = None,
                 *args, **kwargs):
        XtkFrame.__init__(self, master, *args, **kwargs)
        self.win_transparent_color = win_transparent_color
        self.rounded_width = rounded_width
        self.rounded_height = rounded_height
        self.rounded_bg = rounded_bg
        file_path = LIB_PATH + '\\xtkinter\\assets\\' # 获取上级目录
        self.image_path = f'{file_path}{image_name}.png'
        self['background'] = self.win_transparent_color
        # 引用图片
        img = Image.open(self.image_path).resize((self.rounded_width, self.rounded_height))
        self.image = ImageTk.PhotoImage(img)
        self.window_bg_img = tk.Label(self, image=self.image, bg=self.win_transparent_color)
        self.window_bg_img.place(relx=0, rely=0, relwidth=1, relheight=1)

class CanvasRoundedFrame(XtkFrame):
    def __init__(self, master,
                 frame_width: int = 300,
                 frame_height: int = 300,
                 root_bg_color: str = None,  # '#343B61' 此处的透明色一定要设一个与frame_bg相近的色值，并在之后从不使用此值给任何小部件
                 frame_bg:str = None,
                 frame_outline_color:str = '#ffffff',
                 frame_outline_width:int = 2,
                 radii:int = 10,
                 *args, **kwargs):
        XtkFrame.__init__(self,master, *args, **kwargs)
        self.root_bg_color = root_bg_color
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_bg = frame_bg
        self.frame_outline_color = frame_outline_color
        self.frame_outline_width = frame_outline_width
        self.radii = radii
        self['background'] = self.root_bg_color
        label = tk.Label(self, bg=self.root_bg_color, highlightthickness=0)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        img, photo = rounded_rect([self.frame_width, self.frame_height], radius=self.radii, fill=self.frame_bg,
                             outline=self.frame_outline_color, width=self.frame_outline_width)
        label.config(image=photo)
        label.image = photo

class InnerWindowRoundedFrame(XtkFrame):
    def __init__(self, master,
                 rounded_width: int = 300,
                 rounded_height: int = 300,
                 rounded_bg:str = None,
                 rounded_outline_color:str = '#ffffff',
                 rounded_outline_width:int = 2,
                 radii:int = 10,
                 *args, **kwargs):
        XtkFrame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.rounded_width = rounded_width
        self.rounded_height = rounded_height
        self.rounded_bg = rounded_bg
        self.rounded_outline_color = rounded_outline_color
        self.rounded_outline_width = rounded_outline_width
        self.radii = radii
        self['background'] = self.master['background']
        label = tk.Label(self, bg=self.master['background'], highlightthickness=0)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        img, photo = rounded_rect([self.rounded_width, self.rounded_height], radius=self.radii, fill=self.rounded_bg,
                             outline=self.rounded_outline_color, width=self.rounded_outline_width)
        label.config(image=photo)
        label.image = photo

class TitleFrame(tk.Frame):
    def __init__(self, master,
                 title_width:int,
                 title_bg:str,
                 title_icon:str=None,
                 title_text:str=None,
                 inner_bd:int = 4,
                 title_height:int = 28,
                 *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.title_width = title_width
        self.title_height = title_height
        self.title_bg = title_bg
        self['bg'] = title_bg
        icon_image = Image.open(title_icon)
        self.photo = ImageTk.PhotoImage(icon_image)
        self.title_icon = tk.Label(self, image=self.photo, bg=title_bg)
        self.title_icon.place(x=inner_bd, y=inner_bd, width=title_height-inner_bd, height=title_height-inner_bd)
        self.title_text = tk.Label(self, text=title_text, bg=title_bg, fg='#BBB')
        self.title_text.place(x=title_height+4, y=inner_bd, height=title_height-2)

        self.min_btn = tk.Label(self, text='-', bg=title_bg, fg='#BBB', font=(30))
        self.min_btn.place(x=title_width-66, y=inner_bd, width=30, height=title_height-1.5*inner_bd)
        self.close_btn = tk.Label(self, text='×', bg=title_bg, fg='#BBB', font=(30))
        self.close_btn.place(x=title_width-34, y=inner_bd, width=30, height=title_height-1.5*inner_bd)

        self.close_btn.bind("<Enter>", self.on_enter)
        self.close_btn.bind("<Leave>", self.on_leave)
        self.min_btn.bind("<Enter>", self.on_enter)
        self.min_btn.bind("<Leave>", self.on_leave)

    def on_enter(self, enevt):
        if enevt.widget == self.close_btn:
            self.close_btn.configure(bg='#ec4141', fg='#fff')
        if enevt.widget == self.min_btn:
            self.min_btn.configure(bg='#ec4141', fg='#fff')
    def on_leave(self, enevt):
        if enevt.widget == self.close_btn:
            self.close_btn.configure(bg=self.title_bg, fg='#BBB')
        if enevt.widget == self.min_btn:
            self.min_btn.configure(bg=self.title_bg, fg='#BBB')

class topTitleFrame(tk.Frame):
    def __init__(self, master,
                 title_width:int,
                 title_bg:str,
                 title_icon:str=None,
                 title_text:str=None,
                 inner_bd:int = 4,
                 title_height: int = 28,
                 *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)
        self.title_width = title_width
        self.title_height = title_height
        self.title_bg = title_bg
        self['bg'] = title_bg
        icon_image = Image.open(title_icon)
        self.photo = ImageTk.PhotoImage(icon_image)
        self.title_icon = tk.Label(self, image=self.photo, bg=title_bg)
        self.title_icon.place(x=inner_bd, y=inner_bd, width=title_height-inner_bd, height=title_height-inner_bd)
        self.title_text = tk.Label(self, text=title_text, bg=title_bg, fg='#BBB')
        self.title_text.place(x=title_height+4, y=inner_bd, height=title_height-2)
        self.close_btn = tk.Label(self, text='×', bg=title_bg, fg='#BBB', font=(30))
        self.close_btn.place(x=title_width-34, y=inner_bd, width=30, height=title_height-2*inner_bd)

        self.close_btn.bind("<Enter>", self.on_enter)
        self.close_btn.bind("<Leave>", self.on_leave)


    def on_enter(self, enevt):
        if enevt.widget == self.close_btn:
            self.close_btn.configure(bg='#ec4141', fg='#fff')
    def on_leave(self, enevt):
        if enevt.widget == self.close_btn:
            self.close_btn.configure(bg=self.title_bg, fg='#BBB')

if __name__ == '__main__':
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes('-transparentcolor',
                   '#343B61')  # 此处用的color是与要使用的色值相似的值，比如如果使用 #ec4141,则color就设为#ec4142
    root.geometry('1000x500')
    windows_frame = XtkRoundedFrame(root, frame_width=1000, frame_height=500, transparent_color='#343B61', frame_bg='#343B48',
                                    radii=80, dpi=300, image_name='window')
    windows_frame.place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()