import tkinter
from functools import partial

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World!', font="Arial 20 bold")
# b1 = tkinter.Button(root, fg='white', bg='blue', text='Button 1')
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
b3 = MyButton(text='Button 3')
b4 = MyButton(text='quit', command=root.quit)
for item in (lb1, b1, b2, b3, b4):
    item.pack()
root.mainloop()
