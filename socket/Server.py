from socket import *
from threading import *
from datetime import *
import sqlite3

dict_history = []
def tcplink(sock, addr):
    db = sqlite3.connect('d:/msg.db')
    while 1:
        global msgid
        data = sock.recv(1024)
        data = data.decode('utf-8')
        if data == 'exit':
            break
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #列表存储
        new_msg = {}
        new_msg["id"] = msgid
        new_msg["msg"] = data
        new_msg["user"] = addr[0] + str(addr[1])
        new_msg["time"] = time
        dict_history.append(new_msg)
        print(new_msg)
        #print(dict_history)
        #数据库存储
        values = tuple(new_msg.values())
        tuple_list = []
        tuple_list.append(values)
        #print(tuple_list)
        cursor = db.cursor()
        cursor.executemany('insert into msg(id, msg, user, time) values(?,?,?,?)', tuple_list)
        cursor.close()
        db.commit()
        msgid += 1
##        if not data or data == 'exit':
##            break
    sock.close()
    db.close()

db = sqlite3.connect('d:/msg.db')
cursor1 = db.cursor()
cursor1.execute('create table if not exists msg (id varchar(50) primary key, msg varchar(50), user varchar(50), time varchar(50))')
cursor1.close()
db.commit()
cursor2 = db.cursor()
cursor2.execute('select * from msg')
all_list = cursor2.fetchall()
msgid = len(all_list) + 1
cursor2.close()
db.commit()
db.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)
while 1:
    sock, addr = s.accept()
    t = Thread(target = tcplink, args = (sock, addr))
    t.start()
db.close()
