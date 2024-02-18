# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
# Standard library 标准库
import os
from shutil import copytree, rmtree
# Packages 包
from PIL import Image, ImageEnhance
# 项目模块
from . import utils
from .utils import get_file_directory

class XTkThemedBaseClass(object):
    """
    主题操作的基础类
    """
    def __init__(self, tk_interpreter):
        """
        初始化属性并调用_load_themes
        param tk_interpreter：tk解释器。即使只是一个小部件的更改也会影响具有相同父Tk实例的所有小部件。
        """
        self.tk = tk_interpreter
        self._load_themes()

    def _load_themes(self):
        """将主题加载到Tkinter解释器中,并设置默认主题"""
        with utils.temporary_chdir(utils.get_file_directory()):
            self._append_theme_dir("themes")
            self.tk.eval("source themes/pkgIndex.tcl")  # Eval是用于创造和运行脚本的通用构造，此句在Tcl脚本中加载名为"themes/pkgIndex.tcl"的包索引文件

        # self.tk.call("package", "require", "ttk::theme::arc")   # 设置的默认的主题

    # 将主题目录附加到Tk解释器的auto_path
    def _append_theme_dir(self, name):
        path = "[{}]".format(get_file_directory() + "/" + name)
        self.tk.call("lappend", "auto_path", path)

    # 获取主题列表
    def get_themes(self):
        """返回可用主题的名称列表"""
        # return list(set(self.tk.call("ttk::themes")) - self._EXCLUDED)
        return list(self.tk.call("ttk::themes"))

    # get_themes的别名，获取主题列表
    @property
    def themes(self):
        """get_themes（）的属性别名"""
        return self.get_themes()

    # 设置主题
    def set_theme(self, theme_name):
        """
        设置要使用的新主题。使用直接的tk调用来允许使用此包提供的主题。
        :param theme_name: 要激活的主题的名称
        """
        self.tk.call("package", "require", "ttk::theme::{}".format(theme_name))
        self.tk.call("ttk::setTheme", theme_name)

    # 获取当前启用的主题
    @property
    def current_theme(self):
        """获取当前启用的主题"""
        return self.tk.eval("return $ttk::currentTheme")

def main():
    pass


if __name__ == '__main__':
    main()
