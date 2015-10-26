# -*- coding: utf-8 -*-

import time
from sys import exit

print "欢迎来到Miss Python的秘密日记"
psw = "1234"
guess = str(raw_input('四位数暗号：'))

if guess == psw:
    print 'Welcome'

    print "选择：a.回顾过往 ; b.书写现在 ; c.创造未来"

    choose = raw_input('~(～o￣▽￣)～o 。。')

    if choose == 'a':
       f = open("misspython.txt","r")
       diary = f.read()
       print(diary)


    elif choose == 'b':
        f = open ("misspython.txt","a")
        diary = raw_input('>>>') 
        f.write(time.strftime('%Y/%m/%d') + " " + diary)  
        print(diary)
        print "已保存，Adios"
 
    elif choose == 'c':
        print "好好学习，Adios"
        exit()


else:
    print '不对，Adios'
    exit()


f.close()
