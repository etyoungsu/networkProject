from socket import *

soc = socket(AF_INET, SOCK_DGRAM)
host = '172.30.1.30'
port = 12219

while True:
    c = input(">>>")
    soc.sendto(c.encode('utf-8'), (host, port))
    if c == '퇴장':
        break
    print('[응답 대기중..]')
    data, addr = soc.recvfrom(1024)
    print(addr[1], ':', data.decode('utf-8'))
soc.close()