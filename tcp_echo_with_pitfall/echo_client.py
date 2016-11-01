# coding=utf8
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    data_to_sent = 'hello tcp socket'
    try:
        sock.connect(('', 5600))

        total_send = 0
        content_length = len(data_to_sent)
        while total_send < content_length:
            sent = sock.send(data_to_sent[total_send:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_send += total_send + sent

        print(sock.recv(1024))
    finally:
        sock.close()
        print('socket closed')

