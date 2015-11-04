# -*- coding: utf-8 -*-

import socket

s = socket.socket()

host = socket.gethostname()
port = 8088
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	print '通过这个地址开始连接', addr
	c.send('恭喜，连接成功！')
	c.close()
