# -*- coding: utf-8 -*-
# author: aJiea
# web: diary

from bottle import route, run
@route('/')
@route('/index.html')
def index():
    return '〈a href="/welcome"〉转到“Miss Python秘密日记”页面〈/a〉'
@route('/welcome')
def welcome():
    return '欢迎来到Miss Python的秘密日记！'
run(host = 'localhost', port = 8080)

'''
import time
from sys import exit

print "欢迎来到Miss Python的秘密日记"
psw = "1234"
guess = str(raw_input('四位数暗号：'))

if guess == psw:
    print 'Welcome!'

    print "选择题：a.回顾过往 ; b.书写现在 ; c.创造未来"

    choose = raw_input('想好没~(～o￣▽￣)～o 。。')

    if choose == 'a':
       f = open("misspython.txt","r")
       diary = f.read()
       print(diary)


    elif choose == 'b':
        f = open ("misspython.txt","a")
        diary = raw_input('>>>') 
        f.write("\n" + time.strftime('%Y/%m/%d') + " " + diary + "\n")  
        print diary
        print "已保存，Adios！"
 
    elif choose == 'c':
        print "好好学习，Adios！"
        exit()


else:
    print '不对，Adios！'
    exit()


    f.close()
'''
