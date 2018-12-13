import tkinter
from functools import partial

root = tkinter.Tk()  # 相当于创建一个窗体
lb = tkinter.Label(root, text="Hello World!", font="Arial 20")  # 创建label
b1 = tkinter.Button(root, bg='blue', fg='white', text='Button 1')
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b2 = MyButton(text='Button 2')
b3 = MyButton(text='Button 3')
b4 = MyButton(text='QUIT', command=root.quit)
for item in [lb, b1, b2, b3, b4]:
    item.pack()

root.mainloop()
