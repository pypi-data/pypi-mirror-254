# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import os
import re
import json
import site
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor
from .xtk_themes import ThemedStyle
from ..utility.utility_func import rounded_rect
from ..windows.xtk_tk import *

from PIL import Image, ImageTk

LIB_PATH = site.getsitepackages()[1]

def get_dires(path):
    all_items = os.listdir(path)
    dires = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return dires

def get_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file= file.split(".")[0]
            all_files.append(file)
    return all_files

def theme_attribute():

    return ['fg', 'bg', 'disabledbg', 'disabledfg', 'selectbg', 'selectfg', 'window', 'focuscolor', 'checklight', 'cboxbg'
            ]

def theme_widgets():

    return ['Button', 'Checkbutton', 'Radiobutton', 'Scrollbar', 'Scale', 'Entry', 'Labelframe', 'Menubutton', 'Combobox',
            'Spinbox', 'Notebook', 'Progressbar', 'Treeview', 'Frame', 'Label', 'PanedWindow', 'Separator', 'Sizegrip']

def widget_attribute(widget):
    if widget == 'Button':
        return ['button-normal', 'button-pressed', 'button-hover', 'button-disabled']
    if widget == 'Checkbutton':
        return ['checkbox-unchecked', 'checkbox-checked', 'checkbox-unchecked-disabled', 'checkbox-checked-disabled']
    if widget == 'Radiobutton':
        return ['radio-unchecked', 'radio-checked', 'radio-unchecked-disabled', 'radio-checked-disabled']
    if widget == 'Scrollbar':
        return ['trough-scrollbar-horiz', 'trough-scrollbar-vert', 'slider-horiz-normal', 'slider-horiz-disabled', 'slider-horiz-pressed',
                'slider-horiz-hover', 'slider-vert-normal', 'slider-vert-disabled', 'slider-vert-pressed', 'slider-vert-hover']
    if widget == 'Scale':
        return ['trough-horiz-scale-active', 'trough-horiz-scale-disabled', 'trough-vert-scale-active', 'trough-vert-scale-disabled',
                'scale-slider-normal', 'scale-slider-disabled', 'scale-slider-active']
    if widget == 'Entry':
        return ['entry-normal', 'entry-focus', 'entry-disabled']
    if widget == 'Labelframe':
        return ['labelframe']
    if widget == 'Menubutton':
        return ['Menubutton-normal', 'Menubutton-pressed', 'Menubutton-hover', 'Menubutton-disabled', 'arrow-down-normal',
                'arrow-down-active', 'arrow-down-disabled']
    if widget == 'Combobox':
        return ['combo-normal-entry', 'combo-focus-entry', 'combo-disabled-entry', 'readonly-combo-normal', 'readonly-combo-hover',
                'readonly-combo-focus', 'readonly-combo-pressed', 'readonly-combo-disabled', 'combo-normal-button', 'combo-pressed-button',
                'combo-hover-button', 'combo-disabled-button', 'arrow-down-normal', 'arrow-down-active', 'arrow-down-disabled']
    if widget == 'Spinbox':
        return ['spinbox-normal-entry', 'spinbox-focus-entry', 'spinbox-uparrow-btn-normal', 'spinbox-uparrow-btn-pressed', 'spinbox-uparrow-btn-hover',
                'spinbox-uparrow-btn-disable', 'spinbox-small-uparrow', 'spinbox-small-uparrow-active', 'spinbox-small-uparrow-disabled',
                'spinbox-down-btn-normal', 'spinbox-down-btn-pressed', 'spinbox-down-btn-hover', 'spinbox-down-btn-disable', 'spinbox-small-down',
                'spinbox-small-down-pressed', 'spinbox-small-down-pressed', 'spinbox-small-down-disabled']

    if widget == 'Notebook':
        return ['notebook-client', 'notebook-tab-top', 'notebook-tab-selected', 'notebook-tab-hover']
    if widget == 'Progressbar':
        return ['progressbar-trough-hori', 'progressbar-pbar-hori', 'progressbar-trough-vert', 'progressbar-pbar-vert']
    if widget == 'Treeview':
        return ['treeview-not-selected', 'treeview-selected', '']
    if widget == 'Frame':
        return []
    if widget == 'Label':
        return []
    if widget == 'PanedWindow':
        return []
    if widget == 'Separator':
        return []
    if widget == 'Sizegrip':
        return []

def read_tcl(path):
    with open(path, 'r', encoding='utf-8') as file:
        tcl_content = file.read()
    temp = tcl_content.split('array set colors')[1].split('proc LoadImages')[0]
    temp = temp.replace(' "', ':"').replace('\t"', ':"').replace(' ', '').replace('\n', ',').replace('-', '').replace('{,', '', 1).split(',},')[0].split(',')
    colors = []
    attrs = []
    for var in temp:
        attrs.append(var.split(':')[0])
        colors.append(var.split(':')[1].replace('"', ''))

    return attrs, colors

def create_tcl_file(template_file, dst_file, new_name):
    with open(LIB_PATH + '/xtkinter/xtkthemes/template/' + template_file, 'r', encoding='utf-8') as file:
        tcl_content = file.read()

    tcl_content = tcl_content.format(themeTemplate=new_name)
    # 明天修改tcl文件 将新的名字加入文件中，并将新的模版加到主文件中

    with open(dst_file, 'w', encoding='utf-8') as file:
        file.write(tcl_content)

    with open(LIB_PATH + '/xtkinter/xtkthemes/themes/pkgIndex.tcl', 'r', encoding='utf-8') as file:
        tcl_content = file.read()

    new_line = new_name + ' 0.1'
    tcl_content = tcl_content.replace('array set base_themes {', 'array set base_themes {' + '\n'+ f'  {new_line}')

    with open(LIB_PATH + '/xtkinter/xtkthemes/themes/pkgIndex.tcl', 'w', encoding='utf-8') as file:
        file.write(tcl_content)

def write_tcl(datas, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tcl_content = file.read()

    tcl_content = tcl_content.replace('{', '{{').replace('}', '}}')
    tcl_content = re.sub(r'#[0-9a-fA-F]{6}', '{}', tcl_content, len(datas)).format(*datas)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(tcl_content)

class mainLayout:
    def __init__(self, master,):
        self.master = master
        tframe = ttk.Frame(self.master, padding=5)
        tframe.place(x=0, y=0, relwidth=1, height=90)
        theme_name_group = ttk.Labelframe(
            master=tframe, padding=10, text="主题名称",
        )
        theme_name_group.place(x=0, y=0, relwidth=1, height=80)
        theme_label = ttk.Label(theme_name_group, text="Select or Input a theme:")
        theme_label.pack(side=tk.LEFT, padx=20)
        self.themes = get_dires(LIB_PATH + '/xtkinter/xtkthemes/themes')
        self.themes.remove('arc')
        self.theme_cbo = ttk.Combobox(master=theme_name_group, text='xttk', values=self.themes,
                           exportselection=False)
        self.theme_cbo.pack(side=tk.LEFT, fill=tk.X, pady=5)
        self.theme_cbo.current(self.themes.index('xttk'))
        self.theme_cbn_var = tk.BooleanVar()
        self.theme_cbn = ttk.Checkbutton(theme_name_group, text="创建新主题", variable=self.theme_cbn_var, command=self.theme_cbn_click)
        self.theme_cbn.pack(side=tk.LEFT, padx=10)
        theme_label1 = ttk.Label(theme_name_group, text="基于模版:")
        theme_label1.pack(side=tk.LEFT, padx=20)
        self.themeTemplate = get_files(LIB_PATH + '/xtkinter/xtkthemes/template')
        self.theme_cbo1 = ttk.Combobox(master=theme_name_group, text=self.themeTemplate[0], values=self.themeTemplate,
                                      exportselection=False, state='disabled')  # normal
        self.theme_cbo1.pack(side=tk.LEFT, fill=tk.X, pady=5)
        self.theme_cbo1.current(0)
        self.theme_btn = ttk.Button(master=theme_name_group, text="新建 / 修改", command=self.newBtnClick)
        self.theme_btn.pack(side=tk.LEFT, fill=tk.X, pady=5, padx=20)

        dframe = ttk.Frame(self.master, padding=5)
        dframe.place(x=0, y=90, relwidth=1, height=600)
        image_creator_group = ttk.Labelframe(
            master=dframe, padding=5, text="主题的图形化属性",
        )
        image_creator_group.place(x=612, y=0, width=570, height=550)
        image_name_frame = ttk.Frame(image_creator_group)
        image_name_frame.place(x=0, y=0, relwidth=1,height=40)
        image_label1 = ttk.Label(image_name_frame, text="Select a widget :")
        image_label1.pack(side=tk.LEFT, padx=10)
        self.theme_widgets = theme_widgets()
        self.image_cbo1 = ttk.Combobox(master=image_name_frame, text='', values=self.theme_widgets,
                                      exportselection=False, state='readonly')
        self.image_cbo1.pack(side=tk.LEFT, fill=tk.X, pady=0)
        self.image_cbo1.bind("<<ComboboxSelected>>", self.image_cbo1_selected)
        image_label2 = ttk.Label(image_name_frame, text="Select a attr :")
        image_label2.pack(side=tk.LEFT, padx=20)
        self.image_cbo2 = ttk.Combobox(master=image_name_frame, text='', values=[],
                                       exportselection=False, state='readonly')
        self.image_cbo2.pack(side=tk.LEFT, fill=tk.X)

        upload_image_frame = ttk.Frame(image_creator_group)
        upload_image_frame.place(x=0, y=70, relwidth=1, height=40)
        upload_image_label = ttk.Label(upload_image_frame, text="上传自有图片   :")
        upload_image_label.place(x=10, y=5, width=90, height=30)
        self.upload_image_entry = ttk.Entry(upload_image_frame)
        self.upload_image_entry.place(x=110, y=5, width=120, height=30)
        self.upload_image_label = ttk.Label(upload_image_frame, anchor=tk.CENTER, background='#bbbbbb')
        self.upload_image_label.place(x=243, y=5, width=30, height=30)
        self.upload_image_btn1 = ttk.Button(master=upload_image_frame, text="...", command=self.openImage)
        self.upload_image_btn1.place(x=285, y=5, width=35, height=30)
        self.upload_image_btn2 = ttk.Button(master=upload_image_frame, text="上                 传", command=self.uploadImage)
        self.upload_image_btn2.place(x=332, y=5, width=225, height=30)

        create_image_frame = ttk.Frame(image_creator_group, padding=5)
        create_image_frame.place(x=0, y=135, relwidth=1, height=385)
        create_image_attr_group = ttk.Labelframe(
            master=create_image_frame, padding=(5, 10), text="自 定 义 矩 形 图 片", labelanchor="n"
        )
        create_image_attr_group.place(x=0, y=0, relwidth=1, height=335)
        width_label = ttk.Label(create_image_attr_group, text="图片宽度 :")
        width_label.place(x=0, y=5, width=60, height=30)
        self.width_entry = ttk.Entry(create_image_attr_group)
        self.width_entry.place(x=65, y=5, width=50, height=30)
        height_label = ttk.Label(create_image_attr_group, text="图片高度 :")
        height_label.place(x=125, y=5, width=60, height=30)
        self.height_entry = ttk.Entry(create_image_attr_group)
        self.height_entry.place(x=190, y=5, width=50, height=30)
        explanatory_label = ttk.Label(create_image_attr_group, text="( 图片宽高建议在30x30以内，比如按钮背景图26x24 )", foreground='#bbbbbb')
        explanatory_label.place(x=245, y=5, width=290, height=30)

        outline_width_label = ttk.Label(create_image_attr_group, text="边框宽度 :")
        outline_width_label.place(x=0, y=55, width=60, height=30)
        self.outline_width_entry = ttk.Entry(create_image_attr_group)
        self.outline_width_entry.place(x=65, y=55, width=50, height=30)
        outline_color_label = ttk.Label(create_image_attr_group, text="边框颜色 :")
        outline_color_label.place(x=125, y=55, width=60, height=30)
        self.outline_color_entry = ttk.Entry(create_image_attr_group)
        self.outline_color_entry.place(x=190, y=55, width=70, height=30)
        fill_color_label = ttk.Label(create_image_attr_group, text="填充颜色 :")
        fill_color_label.place(x=270, y=55, width=60, height=30)
        self.fill_color_entry = ttk.Entry(create_image_attr_group)
        self.fill_color_entry.place(x=335, y=55, width=70, height=30)
        explanatory_label1 = ttk.Label(create_image_attr_group, text="( 如：#ffffff 或 red )",
                                      foreground='#bbbbbb')
        explanatory_label1.place(x=415, y=55, width=120, height=30)

        radius_size_label = ttk.Label(create_image_attr_group, text="圆角大小 :")
        radius_size_label.place(x=0, y=105, width=60, height=30)
        self.radius_size_entry = ttk.Entry(create_image_attr_group)
        self.radius_size_entry.place(x=65, y=105, width=50, height=30)
        explanatory_label2 = ttk.Label(create_image_attr_group, text="( 0 为直角, 数值越大圆角越大，但不要大于宽高最小值的一半; )",
                                       foreground='#bbbbbb')
        explanatory_label2.place(x=130, y=105, width=380, height=30)

        create_image_label = ttk.Label(create_image_attr_group, text="图片预览:")
        create_image_label.place(x=0, y=155, width=60, height=30)
        self.image_preview_label = ttk.Label(create_image_attr_group, anchor=tk.CENTER, background='#bbbbbb')
        self.image_preview_label.place(x=65, y=155, width=30, height=30)
        self.image_preview_btn2 = ttk.Button(master=create_image_attr_group, text="生     成     图     片",
                                            command=self.previewImage)
        self.image_preview_btn2.place(x=130, y=155, width=225, height=30)

        self.create_image_btn = ttk.Button(master=create_image_frame, text="保                   存",
                                            command=self.createImage)
        self.create_image_btn.pack(side=tk.BOTTOM, fill=tk.X)#, expand=tk.YES

        theme_attribute_group = ttk.Labelframe(
            master=dframe, padding=10, text="主题的颜色属性",
        )
        theme_attribute_group.place(x=0, y=0, width=600, height=550)
        theme_attr_left = ttk.Frame(theme_attribute_group)
        theme_attr_left.place(x=0, y=0, width=298, height=480)
        theme_attr_right = ttk.Frame(theme_attribute_group)
        theme_attr_right.place(x=290, y=0, width=298, height=480)
        self.attr_rows = []
        i = 0
        tcl_path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + self.theme_cbo.get() + '/' + self.theme_cbo.get() + '.tcl'
        attrs, color = read_tcl(tcl_path)
        for attr in attrs:
            if i >9:
                row = AttrRow(theme_attr_right, attr)
                row.pack(fill=tk.BOTH, expand=tk.YES)
            else:
                row = AttrRow(theme_attr_left, attr)
                row.pack(fill=tk.BOTH, expand=tk.YES)
            self.attr_rows.append(row)
            i += 1

        self.theme_attribute_btn = ttk.Button(master=theme_attribute_group, text="应                 用",
                                            command=self.applyAttr)
        self.theme_attribute_btn.pack(side=tk.BOTTOM, fill=tk.X)#, expand=tk.YES

    def previewImage(self):
        img, image = rounded_rect([int(self.width_entry.get()), int(self.height_entry.get())], radius=int(self.radius_size_entry.get()), fill=self.fill_color_entry.get(),
                     outline=self.outline_color_entry.get(), width=int(self.outline_width_entry.get()))
        self.image_preview_label.config(image=image)
        self.image_preview_label.image = image


    def createImage(self):
        image_cbo2_var = self.image_cbo2.get()
        if image_cbo2_var == '':
            # print('请选择一张要修改或创建的图片名')
            messagebox.showinfo('提示', '请在上面选择要创建的图片名称！')
            return
        else:
            path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + self.theme_cbo.get() + '/' + self.theme_cbo.get() + '/' + image_cbo2_var + '.png'
        if self.width_entry.get() == '':
            messagebox.showinfo('提示', '宽度不能为空！')
            return
        if self.height_entry.get() == '':
            messagebox.showinfo('提示', '高度不能为空！')
            return
        if self.radius_size_entry.get() == '':
            messagebox.showinfo('提示', '圆角大小不能为空！')
            return
        if self.fill_color_entry.get() == '':
            messagebox.showinfo('提示', '填充色不能为空！')
            return
        if self.outline_color_entry.get() == '':
            messagebox.showinfo('提示', '边框色不能为空！')
            return
        if self.outline_width_entry.get() == '':
            messagebox.showinfo('提示', '边框宽度不能为空！')
            return

        img, image = rounded_rect([int(self.width_entry.get()), int(self.height_entry.get())],
                           radius=int(self.radius_size_entry.get()), fill=self.fill_color_entry.get(),
                           outline=self.outline_color_entry.get(), width=int(self.outline_width_entry.get()))

        img.save(path)
        messagebox.showinfo('提示', '图片保存成功！')

    def image_cbo1_selected(self, enevt):
        widget = self.image_cbo1.get()
        self.widget_attr = widget_attribute(widget)
        self.image_cbo2['values'] = self.widget_attr
        if self.widget_attr:
            self.image_cbo2.current(0)

    def applyAttr(self):
        # 应用属性
        attrs = []
        for attr in self.attr_rows:
            attrs.append(attr.entry.get())
        tcl_path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + self.theme_cbo.get() + '/' + self.theme_cbo.get() + '.tcl'
        write_tcl(attrs, tcl_path)
        messagebox.showinfo('提示', '应用成功！')

    def theme_cbn_click(self):
        if self.theme_cbn_var.get():
            self.theme_cbo1['state'] = 'readonly'
        else:
            self.theme_cbo1['state'] = 'disabled'

    def uploadImage(self):
        image_cbo2_var = self.image_cbo2.get()

        if image_cbo2_var:
            dst_file_path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + self.theme_cbo.get() + '/' + self.theme_cbo.get() + '/' + image_cbo2_var + '.png'
            shutil.copy(self.file_path, dst_file_path)
            messagebox.showinfo('提示', '图片上传成功！')
        else:
            # print('请选择要修改的图片名称！')
            messagebox.showinfo('提示', '请在上面选择要修改的图片！')

    def openImage(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.gif;*.png")])
        if self.file_path:
            self.upload_image_entry.delete(0, tk.END)
            self.upload_image_entry.insert(0, self.file_path)
            image = Image.open(self.file_path)
            photo = ImageTk.PhotoImage(image)
            self.upload_image_label.config(image=photo)
            self.upload_image_label.image = photo

        return self.file_path

    def newBtnClick(self,):
        theme_cbo_var = self.theme_cbo.get()
        theme_cbo_var1 = self.theme_cbo1.get()
        theme_cbn_var = self.theme_cbn_var.get()
        tcl_path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + self.theme_cbo.get() + '/' + self.theme_cbo.get() + '.tcl'
        def _update():
            attrs, colors = read_tcl(tcl_path)
            for i, attr_row in enumerate(self.attr_rows):
                attr_row.entry.delete(0, tk.END)  # 删除原有内容
                attr_row.entry.insert(0, colors[i])  # 插入新的内容
                attr_row.show.configure(background=colors[i])
            self.image_cbo1.current(0)
            widget = self.image_cbo1.get()
            self.widget_attr = widget_attribute(widget)
            self.image_cbo2['values'] = self.widget_attr
            if self.widget_attr:
                self.image_cbo2.current(0)

        if theme_cbo_var in self.themes:
            if theme_cbn_var is True:
                # print('该主题已经存在, 请点击取消“创建新主题”！')
                messagebox.showinfo("提示", "该主题已经存在, 不能创建新主题！")
                return
            else:
                _update()
        else:
            if theme_cbn_var is True:
                path = LIB_PATH + '/xtkinter/xtkthemes/themes/' + theme_cbo_var
                if not os.path.exists(path):
                    os.mkdir(path)
                path = path + '/' + theme_cbo_var
                if not os.path.exists(path):
                    # os.mkdir(path)
                    shutil.copytree(LIB_PATH + '/xtkinter/xtkthemes/template/themeTemplate', path)
                template_file =theme_cbo_var1 + '.tcl'
                dst_file = path + '.tcl'
                new_template_name = self.theme_cbo.get()
                if not os.path.exists(dst_file):
                    create_tcl_file(template_file, dst_file, new_template_name)
                    # shutil.copyfile('./template/' + template_file, dst_file)
                self.themes = get_dires(LIB_PATH + '/xtkinter/xtkthemes/themes')
                self.themes.remove('arc')
                self.theme_cbo['values'] = self.themes
                _update()
                messagebox.showinfo("提示", "主题创建成功!")
            else:
                # print('请点击“创建新主题”, 并选择基于的主题!')
                messagebox.showinfo("提示", "如需创建新主题, 请点击“创建新主题”, 并选择基于的主题!")


class AttrRow(ttk.Frame):
    def __init__(self, master, attr):
        super().__init__(master, padding=(5, 2))
        self.attr_name = attr

        self.label = ttk.Label(self, text=self.attr_name)
        self.label.place(x=5, y=5, width=75, height=30)
        self.show = tk.Frame(master=self, background='#bbb')
        self.show.place(x=85, y=5, width=15, height=30)
        self.entry = ttk.Entry(self)
        self.entry.place(x=105, y=5, width=120, height=30)
        self.entry.bind("<FocusOut>", self.enter_color)
        self.color_picker = ttk.Button(master=self,text="...", command=self.pick_color)
        self.color_picker.place(x=230, y=5, width=35, height=30)

        # 初始化
        # self.color_value = self.style.colors.get(color)
        # self.update_patch_color()

    def pick_color(self):
        color = askcolor(color='#bbbbbb')
        if color[1]:
            self.color_value = color[1]
            self.update_patch_color()
        self.event_generate("<<ColorSelected>>")

    def enter_color(self, *_):
        try:
            self.color_value = self.entry.get().lower()
            self.update_patch_color()
        except:
            self.color_value = '#bbbbbb'
            self.update_patch_color()
        self.event_generate("<<ColorSelected>>")

    def update_patch_color(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.color_value)
        self.show.configure(background=self.color_value)

def themeCreator():
    xtk_width = 1200
    xtk_height = 700
    title_height = 30
    inner_bd = 4

    root = CanvasRoundedWindow(win_width=xtk_width, win_height=xtk_height, title='XTk主题创建器', title_frame_bg='#ffffff',
                               title_height=title_height, inner_bd=inner_bd, main_frame_bg='#ffffff',
                               win_transparent_color='#f2f2f2', win_bg='#ffffff', win_outline_color='#bbb',
                               win_outline_width=2, radii=10)
    style = ThemedStyle()
    style.set_theme('xttk')
    # print(style.theme_names())
    # print(style.theme_use())
    mainLayout(root.main_frame)

    root.mainloop()


if __name__ == '__main__':
    themeCreator()