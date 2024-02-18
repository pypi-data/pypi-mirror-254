# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import sys
from ctypes import OleDLL

if sys.version_info < (3, 11):
    raise RuntimeError('本项目基于python3.11版本开发, 低于此版本可能会有错误')

OleDLL('shcore').SetProcessDpiAwareness(2) # 设置系统DPI感知 windows系统专用
"""
参数设置为1时，表示进程将忽略系统的DPI设置，即不进行DPI感知处理。这意味着无论系统使用的是高DPI还是低DPI显示模式，应用程序都将以相同的大小和分辨率运行，
不会自动适应不同的DPI设置。
参数设置为2时，表示进程将根据系统的DPI设置进行自适应调整。这意味着当系统切换到高DPI显示模式时，应用程序将自动放大以适应新的分辨率；
而当系统切换到低DPI显示模式时，应用程序将自动缩小以适应新的分辨率。通过这种方式，应用程序可以在不同的DPI设置下提供更好的用户体验。
"""
