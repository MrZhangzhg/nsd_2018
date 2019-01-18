import tkinter
from functools import partial

def say_hi(word):
    def greet():
        lb1.config(text='Hello %s!' % word)
    return greet

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World!', font="Arial 20 bold")
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1', command=say_hi('China'))
b2 = MyButton(text='Button 2', command=say_hi('Tedu'))
b4 = MyButton(text='quit', command=root.quit)
for item in (lb1, b1, b2, b4):
    item.pack()
root.mainloop()
