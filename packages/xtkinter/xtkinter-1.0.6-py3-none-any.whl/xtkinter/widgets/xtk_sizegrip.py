# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
from tkinter import ttk

class XtkSizegrip(ttk.Sizegrip):
    def __init__(self, master, bg:str, style, **kwargs):
        super().__init__(master, **kwargs)
        self.style = style
        self.style.configure('Custom.TSizegrip', background=bg)
        self.config(style='Custom.TSizegrip')
