# xtkinter

#### 介绍
xtkinter是基于tkinter的python Ui窗口设计模块，是tkinter库的扩展，添加了更灵活的自定义窗口设计以及主题样式的可视化修改

#### 安装教程

1.  可使用pip install xtkinter 下载安装最新该模块
2.  在gitee平台上下载源代码
3.  git clone https://gitee.com/yuhypython/xtkinter.git

#### 案例

1.  用xtkinter的自定义窗口功能开发的窗口，该案例模仿网络上一个用PyQt设计的UI框架，用xtkinter模块也可以轻松实现比较美观的界面，而且代码量很少，非常简单易用。
![输入图片说明](assets/2.png)

2.  该案例是xtkinter基于本身开发的主题创建器themeCreator, 可以使用以下代码打开，并对现有主题修改或创建新的主题，详见使用说明

    `from xtkinter.xtkthemes import themeCreator as thc`

    `thc.themeCreator()`

    调用themeCreator()方法就会打开如下的界面，该界面也基于xtkinter模块自身开发的
    
    ![输入图片说明](assets/1.png)
    
#### 使用说明

    介绍： xtkinter主要分为两部分，一部分是更加灵活的自定义窗口； 另一部分就是主题创建器themeCreator.

第一章：xtkinter 的自定义窗口
    
    1.  主窗口的自定义设计 xtk_tk

        首先是导入模块 from xtkinter.windows import xtk_tk as xtk
    
        说明： 对于窗口的设计，因为原有的tkinter窗口的标题栏及窗口外形无法更多的修改，所以在xtkinter中去掉了原有的tkinter标题        
              栏，然后重新创建标题栏，可以随意设置。所以在使用中如果需要传统的tkinter标题栏，可以直接使用tkinter.Tk() 
              或 使用封装后xtk.Tk()，都是在调用原tkinter的窗口；如果想自定义窗口则使用xtk下的三个窗口对象。
        
        在该模块下有三个窗口对象： 
            CanvasRoundedWindow ：自定义圆角形窗口
                使用 
                    root = xtk.CanvasRoundedWindow() 
                        
                    root.mainloop()
                就可以调用一个简单的圆角形窗口

                而对窗口的设置是通过对象的属性来调整的， 以下是CanvasRoundedWindow对象的属性
                
                icon : 标题的图标，是str类型，为图片的地址,
                title: 标题的内容，str类型,
                title_height : 标题栏的高度 int,
                title_frame_bg:标题栏的背景色,
                main_frame_bg:窗口主框架的背景色,
                inner_bd: 窗口内边框的宽度,
                win_width:窗口的宽度,
                win_height:窗口的高度,
                win_transparent_color: 窗体的透明色，即tkinter中-transparentcolor的属性
                win_bg: 窗体的背景色, 一般和title_frame_bg的值相同,
                win_outline_color: 窗体的外边框的颜色,
                win_outline_width: 窗体的外边框的宽度,
                radii:窗体圆角的大小, 此属性值为0时，窗体为方角，和CornerWindow一样都能做成方角窗口,
                
                举例：
                    root = xtk.CanvasRoundedWindow(icon='xxx/image.png', title='测试', title_height=28, 
                                            title_frame_bg='#21252b', main_frame_bg='#ffffff', inner_bd=2, 
                                            win_width=1200, win_height=800, win_transparent_color='#21253b',
                                            win_bg='#21252b',win_outline_color='#bbbbbb', win_outline_width=2, 
                                            radii=10)
                    
                    root.mainloop()
                此外该对象还包括两个框架，root.title_frame 标题框架 和 root.main_frame 窗口主框架 

            CornerWindow： 自定义方角形窗口，与 CanvasRoundedWindow对象的使用方法相同  


    2.  置顶窗口的自定义设计 xtk_toplevel
        
        这个和xtk_tk相同，同样有CanvasRoundedWindow 和 CornerWindow 两个对象，使用方法同上

    3.  窗体内窗口的自定义设计  xtk_inner_window

        xtk_inner_window 是在主窗体内的窗口，同样也有CanvasRoundedInnerWindow 和 CornerInnerWindow 两个对象，使用方法同上

        ![输入图片说明](assets/3.png)





第二章：主题创建器themeCreator的使用

        xtkinter中提供了一个可视化的修改主题样式的功能，如下图：

        ![输入图片说明](assets/1.png)

        在这里面可以新建或修改主题，这里面只涉及图形化主题，即控件的整体外观都是由图片组成的，所以除了一些颜色属性外，就是图片，比如: 按钮的各种外观，你可以自己上传图片，也可以用自定义生成图片，然后保存。 

        最后使用xtkinter中的样式模块引用你修改或创建的主题，比如：你创建了一个aaaa的主题，就可以用下面的代码设定。

        from xtkinter.xtkthemes.xtk_themes import ThemedStyle

        style = ThemedStyle()
        style.set_theme('xttk')



