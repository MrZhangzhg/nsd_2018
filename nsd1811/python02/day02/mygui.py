import tkinter
from functools import partial

window = tkinter.Tk()
lb = tkinter.Label(window, text="Hello World!", font="Arial 20")
# b1 = tkinter.Button(window, fg='white', bg='blue', text='Button 1')
MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 1')
b3 = MyButton(text='Button 1')
qb = MyButton(text='QUIT', command=window.quit)

lb.pack()
b1.pack()
b2.pack()
qb.pack()

window.mainloop()
