# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import tkinter as tk
from xtkinter.windows import xtk_tk
from xtkinter.windows.xtk_inner_window import *

root = xtk_tk.CanvasRoundedWindow(win_width=800, win_height=450, win_transparent_color='#343B61', win_bg='#343B48', title_frame_bg='#343B48',
                                  win_outline_color='#ffffff', win_outline_width=3, radii=10)

def create_new_window():
    new_window = CornerInnerWindow(root.main_frame, win_width=300, win_height=200, win_outline_color='#ffffff', win_outline_width=2,
                                   title_frame_bg='#343B48', main_frame_bg='#fff000')
    # new_window = CanvasRoundedInnerWindow(root.main_frame, win_width=300, win_height=200, win_bg='#343B48',title_frame_bg='#343B48',main_frame_bg='#343B48',
    #                                       win_outline_color='#ffffff', win_outline_width=2, radii=10)


button = tk.Button(root, text="打开新窗口", command=create_new_window)
button.place(x=370, y=40)

root.mainloop()