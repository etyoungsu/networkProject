from socket import *
import os
import sys

soc = socket(AF_INET, SOCK_STREAM)
host = '172.30.1.30'
port = 12220
soc.connect((host, port))
print(host, '님의 방에 접속되었습니다.')
print((soc.recv(1024)).decode('Utf-8'))

while True:
    fileName = input('전송할 파일 이름은?')
    soc.sendall(fileName.encode('utf-8'))

    data = soc.recv(1024)
    data_transferred = 0
    if data.decode() == "error":
        print("파일 %s 가 존재하지 않는다" % fileName)
        continue

    nowdir = os.getcwd()
    with open(nowdir + "\\" + fileName, 'wb') as f:
        try:
            while data:
                f.write(data)
                data_transferred += len(data)
                data = soc.recv(1024)
        except Exception as ex:
            print(ex)
    print('파일 %s 받기 완료. 전송량 %d' % (fileName, data_transferred))
    break
    soc.close()
