# -*- coding: utf-8 -*-
## {{{ http://code.activestate.com/recipes/578568/ (r1)


from Tkinter import * 
import tkMessageBox
from tkSimpleDialog import askstring
from tkFileDialog  import * 
from tkMessageBox import askokcancel  

#resize函数是用来改变文字大小的，当进度条改变时调用
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())
#config函数就是通过设置组件的参数来改变组件的，这里改变的是font字体大小
root=Tk()   #主窗口
root.title("【Miss Python日记簿】")
root.geometry('800x800')  #设置了主窗口的初始大小
label=Label(root,text='欢迎来到Miss Python的秘密日记',font='Helvetica -5 bold', fg="green")  #设置标签字体的初始大小
label.pack(fill=Y,expand=1)
#scale创建进度条，设置
scale=Scale(root,from_=10,to=35,orient=HORIZONTAL,command=resize)
scale.set(12)  #设置起始位置
scale.pack(fill=X,expand=1)

#设置wedget功能性按钮

class Quitter(Frame):            
    def __init__(self, parent=None):     
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='离', bg='turquoise', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=RIGHT)
    def quit(self):
        ans = askokcancel('重要的事情问两次', "真的要走了？")
        if ans: Frame.quit(self)
class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)        
        self.makewidgets()
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)         
        text.config(yscrollcommand=sbar.set)      
        sbar.pack(side=RIGHT, fill=Y)          
        text.pack(side=LEFT, expand=YES, fill=BOTH)   
        self.text = text
    def settext(self, text='', file=None):
        if file: 
          text = open(file, 'r').read()
        self.text.delete('1.0', END)          
        self.text.insert('1.0', text)         
        self.text.mark_set(INSERT, '1.0')       
        self.text.focus()                
    def gettext(self):                
        return self.text.get('1.0', END+'-1c')     
class SimpleEditor(ScrolledText):            
    def __init__(self, parent=None, file=None): 
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='读', bg='pink', command=self.read).pack(side=LEFT)
        Button(frm, text='存', bg='red', command=self.onSave).pack(side=LEFT)
        Button(frm, text='切', bg='orange', command=self.onCut).pack(side=LEFT)
        Button(frm, text='帖', bg='yellow',command=self.onPaste).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file) 
        self.text.config(font=('courier', 9, 'normal'))
   
    def read(self):
        filename = tkMessageBox.showinfo()
        if filename:
            alltext= self.getread()
            read(filename, 'r').read(alltext)
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()           
            open(filename, 'w').write(alltext)     
    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)    
        self.text.delete(SEL_FIRST, SEL_LAST)      
        self.clipboard_clear()       
        self.clipboard_append(text)
    def onPaste(self):                  
        try:
          text = self.selection_get(selection='CLIPBOARD')
          self.text.insert(INSERT, text)
        except TclError:
          pass                  
  
if __name__ == '__main__':
      try:
        SimpleEditor(file=sys.argv[1]).mainloop()  
      except IndexError:
        SimpleEditor().mainloop()


mainloop()
