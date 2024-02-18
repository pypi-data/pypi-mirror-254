# -*- coding: utf-8 -*-
"""
开发者：于海洋
VX: yuhaiyang2866
QQ：421142953
文件说明：
"""
import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='xtkinter',
    version='1.0.6',
    author='yuhaiyang',
    author_email='421142953@qq.com',
    description='一个基于tkinter包的扩展模块，可以更加自由的定义各种窗口及美化小部件，使用xtkinter包可以做出更漂亮的图形界面',
    long_description_content_type='text/markdown',
    long_description=long_description,  # 模块的详细介绍
    packages=setuptools.find_packages(),    # 自动找到项目中导入的模块
    # include_dirs=['assets'],
    include_package_data=True,
    url='https://gitee.com/yuhypython/xtkinter',
    # 模块相关的元数数（更多描述信息）
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]

)