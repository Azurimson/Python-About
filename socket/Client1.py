from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 12345))
while 1:
    c = input()
    content = c.encode(encoding = 'utf-8')
    s.send(content)
    if c == 'exit':
        break
s.close()
