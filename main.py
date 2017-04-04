#!/usr/bin/python
import os
import socket

site=''
def open_index():
    global site
    try:
        file = open('index.html')
    except IOError as e:
        print(u'не удалось открыть файл')
        for i in os.listdir():
            site=i+'\n'
        return site 
    else:
        for word in file:
            #print(u'нашли файл')
            site=site+word
            return site
        
open_index()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
sock.listen(1)
conn, addr = sock.accept()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn.send(bytes(site,"utf-8"))
