import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

#filename = 'D:/BugReport.txt'
#print('I want to get the file %s!' % filename)
def sendfile(conn):
 str1 = conn.recv(1024)
 filename = str1.decode('utf-8')
 print('The client requests my file:',filename)
 if os.path.exists(filename):
     print('I have %s, begin to download!' % filename)
     conn.send(b'yes')
     conn.recv(1024)
     size = 1024
     with open(filename,'rb') as f:
        while True:
         data = f.read(size)
         conn.send(data)
         if len(data) < size:
           break
     print('%s is downloaded successfully!' % filename)
 else:
     print('Sorry, I have no %s' % filename)
     conn.send(b'no')

#s.send(filename.encode('utf-8'))
sendfile(s)
s.close()
