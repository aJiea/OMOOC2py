#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
import time

@diary('/')
def index():
    return template('index.tpl')

@route('/add', method='get')
def add():
    cnt = request.forms.get('txtadd')
    '''
    if content == 'a':
        file = open('Diary.txt', 'r')
        return template('index.tpl', file=file,content=content) # 打印文档

    else:
        file = open('Diary.txt', 'a+') 
        file.seek(0)
        date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        file.write(date + "\n" + content + "\n\n")
        file.seek(0)
        return template('index.tpl', file=file,content=content)
'''

    debug(True)
run(host='127.0.0.1', port=8080,reloader=True)
