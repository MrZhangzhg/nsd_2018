import tkinter
from functools import partial

def hello():
    lb1.config(text='Hello China!')

def welcome():
    lb1.config(text='Hello Tedu!')

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World!', font="Arial 20 bold")
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1', command=hello)
b2 = MyButton(text='Button 2', command=welcome)
b4 = MyButton(text='quit', command=root.quit)
for item in (lb1, b1, b2, b4):
    item.pack()
root.mainloop()
