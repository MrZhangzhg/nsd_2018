import tkinter
from functools import partial

def pstar():
    print('*' * 30)

def hello():
    lb.config(text='Hello China')

def welcome():
    lb.config(text='Hello Tedu')


def say_hi(word):
    def greet():
        lb.config(text='Hello %s' % word)

    return greet


root = tkinter.Tk()  # 相当于创建一个窗体
lb = tkinter.Label(root, text="Hello World!", font="Arial 20")  # 创建label
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = MyButton(text='Button 1', command=pstar)
b2 = MyButton(text='Button 2', command=say_hi('China'))
b3 = MyButton(text='Button 3', command=say_hi('Tedu'))
b4 = MyButton(text='QUIT', command=root.quit)
for item in [lb, b1, b2, b3, b4]:
    item.pack()

root.mainloop()
