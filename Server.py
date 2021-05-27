from socket import *

soc = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12219
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen()

c, addr = soc.accept()
print(str(addr), '님이 접속하셨습니다.')
notice = '저희 방에 오신 것을 환영합니다'
c.send(notice.encode('utf-8'))

while True:
    print('[응답 대기중..]')
    data = (c.recv(1024)).decode('Utf-8')
    print(addr[1], ':', data)
    if data == '퇴장':
        print(addr[1], '님이 퇴장하셨습니다.')
        break

    s = input(">>>")
    c.send(s.encode('utf-8'))
soc.close()
