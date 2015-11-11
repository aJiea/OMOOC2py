# -*- coding: utf-8 -*-
# author: aJiea
# web: diary

from bottle import route, run, get, post, request


@route('/welcome')
def welcome():
    return '欢迎来到Miss Python的秘密日记！'
run(host = 'localhost', port = 8080)
