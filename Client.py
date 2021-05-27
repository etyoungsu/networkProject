from socket import *

soc = socket(AF_INET, SOCK_STREAM)
host = '172.30.1.30'
port = 12220
soc.connect((host, port))
print(host, '님의 방에 접속되었습니다.')
print((soc.recv(1024)).decode('Utf-8'))

while True:
    c = input(">>>")
    soc.send(c.encode('utf-8'))
    if c == '퇴장':
        break
    print('[응답 대기중..]')
    print('방장 :', (soc.recv(1024)).decode('Utf-8'))
soc.close()
