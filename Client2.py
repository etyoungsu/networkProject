import sys
from socket import *
import threading
import time


def send(sock):
    while True:
        c = input(">>>")
        sock.send(c.encode('utf-8'))
        if c == '퇴장':
            soc.close()
            break


def recieve(sock):
    while True:
        print('방장 :', (sock.recv(1024)).decode('Utf-8'))


soc = socket(AF_INET, SOCK_STREAM)
host = '172.30.1.30'
port = 12231
soc.connect((host, port))
print(host, '님의 방에 접속되었습니다.')
print((soc.recv(1024)).decode('Utf-8'))

sender = threading.Thread(target=send, args=(soc,), daemon=True)
receiver = threading.Thread(target=recieve, args=(soc,), daemon=True)

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
