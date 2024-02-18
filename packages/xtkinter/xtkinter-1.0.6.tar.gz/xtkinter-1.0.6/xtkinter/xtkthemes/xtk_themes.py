# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
# Standard library 标准库
import tkinter as tk
from tkinter import ttk
# 三方包

# 项目模块
from .themed_base_class import XTkThemedBaseClass


class ThemedStyle(ttk.Style, XTkThemedBaseClass):
    """
    继承自ttk.Style,并添加其它自定义主题。
    """
    def __init__(self, *args, **kwargs):
        theme = kwargs.pop("theme", None)       # 如果键存在则删除并返回其值，不存在则返回None
        # 初始化ttk.Style
        ttk.Style.__init__(self, *args, **kwargs)
        # 初始化 基础类
        XTkThemedBaseClass.__init__(self, self.tk)
        # 设置初始主题
        if theme is not None and theme in self.get_themes():
            self.set_theme(theme)

    def theme_use(self, theme_name=None):
        """
        设置新主题以使用或返回当前主题名称

        :param theme_name: name of theme to use
        :returns: active theme name
        """
        if theme_name is not None:
            self.set_theme(theme_name)
        return ttk.Style.theme_use(self)

    def theme_names(self):
        """
        get_themes（）的别名，用于替换普通ttk。样式实例。
        :returns: get_themes()的结果
        """
        return self.get_themes()
