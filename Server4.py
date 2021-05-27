from socket import *

soc = socket(AF_INET, SOCK_DGRAM)
host = gethostname()
port = 12218
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind((host, port))

while True:
    print('[응답 대기중..]')
    data, addr = soc.recvfrom(1024)
    print(addr[1], ':', data.decode('utf-8'))
    if data.decode('utf-8') == '퇴장':
        print(addr[1], '님이 퇴장하셨습니다.')
        break
    s = input(">>>")
    soc.sendto(s.encode('utf-8'), addr)
soc.close()
