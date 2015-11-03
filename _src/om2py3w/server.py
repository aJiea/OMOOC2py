# -*- coding: utf-8 -*-
# author: aJiea
# a diary program


import socket
import sys

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print '链接配置成功！'
except socket.error, msg :
	print '配置错误. 错误代码: ' + str(msg[0]) + ' 错误信息 ' + msg[1]
	sys.exit()


# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print '匹配错误. 错误代码: ' + str(msg[0]) + ' 错误信息 ' + msg[1]
	sys.exit()
	
print '匹配成功！'

#now keep talking with the client
while 1:
	# receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	
	if not data: 
		break

# ================== 以下部分替换即可 =======================

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
    
# ================== 以上部分替换即可 =======================

reply = '好的，收到！' + data
	
s.sendto(reply , addr)
print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	
s.close()
