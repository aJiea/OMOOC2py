# _*_ coding: utf-8 _*_

import urllib

history = open('Diary.txt')
print history.read()
history.close()


while True:
    content = raw_input("content: ")

    if content == 'a':
      now = open('Diary.txt')
      print now.read()
      now.close()

    else:
      values = {"content": content} 
      data = urllib.urlencode(values) 
      url = "http://localhost:8080/add"
      request = urllib2.Request(url, data) 
      response = urllib2.urlopen(request) 
      file = open('Diary.txt','r')
      print file.read()
      file.close()
