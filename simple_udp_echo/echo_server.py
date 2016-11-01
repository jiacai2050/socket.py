# coding=utf8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置 SO_REUSEADDR 后,可以立即使用 TIME_WAIT 状态的 socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 5500))
# 没有调用 listen

if __name__ == '__main__':
    while 1:
        data, addr = sock.recvfrom(1024)

        print('new client from %s:%s' % addr)
        sock.sendto(data, addr)
