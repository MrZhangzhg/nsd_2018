from functools import partial
import tkinter

window = tkinter.Tk()
lb = tkinter.Label(window, text='Hello World')
# b1 = tkinter.Button(window, fg='white', bg='blue', text='button 1')
# 改造tkinter.Button，固定它的一些选项
MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
b1 = MyButton(text='button 1')
b2 = MyButton(text='button 2')
b3 = MyButton(text='button 3', command=window.quit)
for item in (lb, b1, b2, b3):
    item.pack()     # 把4个组件安装到window上
window.mainloop()   # 主程序方法
