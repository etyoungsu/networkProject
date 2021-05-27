import sys
from os.path import exists
from socket import *

soc = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12216
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen()

c, addr = soc.accept()
print(str(addr), '님이 접속하셨습니다.')
notice = '저희 방에 오신 것을 환영합니다'
c.send(notice.encode('utf-8'))


while True:
    fileName = c.recv(1024)
    print('받은 파일데이터 : ', fileName.decode())
    data_transferred = 0

    if not exists(fileName):
        print("파일 없음")
        msg = "error"
        c.send(msg.encode())
        continue

    print('파일 %s 전송' %fileName.decode())
    with open(fileName, 'rb') as f:
        try:
            data = f.read(1024)
            while data:
                data_transferred += c.send(data)
                data = f.read(1024)
        except Exception as ex:
            print(ex)
    print("전송완료 %s, 전송량 %d" %(fileName.decode(), data_transferred))
    break
soc.close()
