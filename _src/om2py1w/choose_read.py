# -*- coding: utf-8 -*-


print '''选择：
a.回顾过往
b.书写现在
c.创造未来

'''
diary = raw_input('~(～o￣▽￣)～o 。。')

if diary == 'a':
   f = open("misspython.txt","r")
   diary = f.read()
   print(diary)
