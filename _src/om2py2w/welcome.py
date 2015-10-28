# -*- coding: utf-8 -*-
# author: aJiea
# a diary program

import Tkinter 
from Tkinter import *
# widgets...
root = Tk()
root.title("【Miss Python's Diary】")
root.geometry('500x500')
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True

label = Label(root, text=">>> 欢迎来到Miss Python的秘密日记 <<<", bg="purple",font=("Ubuntu"), width=400, height=50)
label.pack(side=TOP)
root.mainloop()
