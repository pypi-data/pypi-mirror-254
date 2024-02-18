# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import os
import contextlib

@contextlib.contextmanager  # 用于将一个函数转换为上下文管理器。它通常与 with 语句一起使用，以便在进入和退出代码块时自动调用相应的方法。
def temporary_chdir(new_dir):   # 临时目录
    """
    这段代码是Python中的上下文管理器，用于临时改变当前工作目录。它使用了os模块的getcwd()函数获取当前工作目录，
    并使用chdir()函数将工作目录切换到新的目录。在try语句块中执行需要的操作，然后在finally语句块中将工作目录切换回原来的目录。
    """
    old_dir = os.getcwd()   # 获取当前工作目录
    os.chdir(new_dir)       # 将工作目录切换到新的目录
    try:
        # 在这里执行需要的操作
        # ...
        yield
    finally:
        os.chdir(old_dir)   # 将工作目录切换回原来的目录

# 返回当前文件目录的绝对路径
def get_file_directory():
    """返回当前文件目录的绝对路径"""
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    path = "[{}]".format(get_file_directory() + "/" + 'name')

    print(path)