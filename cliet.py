from socket import socket, AF_INET, SOCK_STREAM
import sys

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("192.168.90.180", 5000))
data = sys.argv[1].encode()
sock.send(data)
data = sock.recv(1024)  # читаем ответ от серверного сокета
sock.close()  # закрываем соединение

predict = data.decode()
print(predict)