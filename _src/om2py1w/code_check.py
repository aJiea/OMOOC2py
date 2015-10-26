# -*- coding: utf-8 -*-

from sys import exit

print "欢迎来到Miss Python的秘密日记"
psw = "1234"
guess = str(raw_input('四位数暗号：'))

if guess == psw:
    print 'Welcome'

else:
    print '不对，再见'
    exit()
