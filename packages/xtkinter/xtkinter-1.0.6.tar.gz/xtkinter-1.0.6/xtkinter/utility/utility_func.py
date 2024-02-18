# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def rounded_rect(size:list[int, int], radius:int =10, fill='red', outline='black', width:int =2):
    x = size[0] * 10
    y = size[1] * 10
    img = Image.new("RGBA", (x, y))
    draw = ImageDraw.Draw(img)
    # radius = min([x, y]) // (2*20)
    draw.rounded_rectangle([0, 0, x - 1, y - 1], radius=radius * 10, fill=fill, outline=outline, width=width * 10)
    resized_image = img.resize(size, Image.BICUBIC)
    image = ImageTk.PhotoImage(resized_image)

    return resized_image, image

def canvas_rounded(canvas:tk.Canvas, radii:int, width:int, height:int, x:int, y:int, color_fill:str, color_outline:str,
             outline_width:int,):
    if 2 * radii > width:
        radii = width // 2
        self.radii = radii
    if 2 * radii > height:
        radii = height // 2
        self.radii = radii

    d = 2 * radii  # 圆角直径
    _x, _y, _w, _h = x + radii, y + radii, width - d, height - d

    # 虚拟控件内部填充颜色
    kw = {'outline': '', 'fill': color_fill}
    self.inside = [
        canvas.create_rectangle(
            x, _y, x + width, y + height - radii, **kw),
        canvas.create_rectangle(
            _x, y, x + width - radii, y + height, **kw),
        canvas.create_arc(
            x, y, x + d, y + d, start=90, **kw),
        canvas.create_arc(
            x + _w, y, x + width, y + d, start=0, **kw),
        canvas.create_arc(
            x, y + _h, x + d, y + height, start=180, **kw),
        canvas.create_arc(
            x + _w-radii, y + _h-radii, x + width, y + height, start=270, **kw)
            ]

    # 虚拟控件外框
    kw = {'extent': 100, 'style': 'arc', 'outline': color_outline}
    self.outside = [
        canvas.create_line(
            _x, y, x + width - radii, y, fill=color_outline, width=outline_width),
        canvas.create_line(
            _x, y + height, x + width - radii, y + height, fill=color_outline, width=outline_width),
        canvas.create_line(
            x, _y, x, y + height - radii, fill=color_outline, width=outline_width),
        canvas.create_line(
            x + width, _y, x + width, y + height - radii + 1, fill=color_outline, width=outline_width),
        canvas.create_arc(
            x, y, x + d, y + d, start=90, width=outline_width, **kw),
        canvas.create_arc(
            x + _w, y, x + width, y + d, start=0, width=outline_width, **kw),
        canvas.create_arc(
            x, y + _h, x + d, y + height, start=180, width=outline_width, **kw),
        canvas.create_arc(
            x + _w-radii, y + _h-radii, x + width, y + height, start=270, width=outline_width, **kw)]