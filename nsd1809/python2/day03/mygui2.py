from functools import partial
import tkinter

# def hello():
#     lb.config(text="Hello China")
#
# def welcome():
#     lb.config(text="Hello TEDU")

def say_hi(word):
    def greet():
        lb.config(text="Hello %s" % word)
    return greet


window = tkinter.Tk()
lb = tkinter.Label(window, text='Hello World', font=("Times", "30"))
MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
b1 = MyButton(text='button 1', command=say_hi('China'))
b2 = MyButton(text='button 2', command=say_hi('TEDU'))
b3 = MyButton(text='button 3', command=window.quit)
for item in (lb, b1, b2, b3):
    item.pack()     # 把4个组件安装到window上
window.mainloop()   # 主程序方法
