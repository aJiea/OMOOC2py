# -*- coding: utf-8 -*-



import socket	#for sockets
import sys	#for exit

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print '不能建立链接'
	sys.exit()

host = 'localhost';
port = 8888;

while(1) :
	import time
from sys import exit

＃＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝以下替换＝＝＝＝＝＝＝＝＝＝
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
＃ ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝以上替换＝＝＝＝＝＝＝＝	
	try :
		#Set the whole string
		s.sendto(msg, (host, port))
		
		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]
		
		print '服务器回复 : ' + reply
	
	except socket.error, msg:
		print '错误代码 : ' + str(msg[0]) + ' 错误信息 ' + msg[1]
		sys.exit()
