import tkinter
from functools import partial

window = tkinter.Tk()   # 窗体
lb = tkinter.Label(window, text="Hello World!", font="Arial, 20")
b1 = tkinter.Button(window, fg='white', bg='blue', text='Button 1')
# 改造tkinter.Button，固定它的几个参数，生成新的MyButton
MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
b2 = MyButton(text="Button 2")
b3 = MyButton(text="Quit", command=window.quit)

lb.pack()   # 执行方法，把创建的label真正的安装在window上
b1.pack()
b2.pack()
b3.pack()

window.mainloop()    # 窗体方法，用于启动GUI界面程序
