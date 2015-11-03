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
	msg = raw_input('Enter message to send : ')
	
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
