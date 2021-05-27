from socket import *
import sys
import time
import threading


def send(sock):
    while True:
        s = input(">>>")
        sock.send(s.encode('utf-8'))


def receive(sock):
    global ck
    while True:
        data = (sock.recv(1024)).decode('Utf-8')
        print(addr[1], ':', data)
        if data == '퇴장':
            print(addr[1], '님이 퇴장하셨습니다.')
            ck = 1
            break


soc = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12230
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen(0)

c, addr = soc.accept()
print(str(addr), '님이 접속하셨습니다.')
notice = '저희 방에 오신 것을 환영합니다'
c.send(notice.encode('utf-8'))
ck = 0

sender = threading.Thread(target=send, args=(c,), daemon=True)
receiver = threading.Thread(target=receive, args=(c,), daemon=True)

sender.start()
receiver.start()

while True:
    time.sleep(1)
    if ck == 1:
        break
soc.close()
