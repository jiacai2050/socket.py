#coding=utf8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
baidu_ip = socket.gethostbyname('baidu.com')
sock.connect((baidu_ip, 80))
print('connected to %s' % baidu_ip)

req_msg = [
    'GET / HTTP/1.1',
    'User-Agent: curl/7.37.1',
    'Host: baidu.com',
    'Accept: */*',
]
delimiter = '\r\n'

sock.send(delimiter.join(req_msg))
sock.send(delimiter)
sock.send(delimiter)

print('%sreceived%s' % ('-'*20, '-'*20))
http_response = sock.recv(4096)
print(http_response)
