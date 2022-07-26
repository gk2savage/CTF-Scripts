#!/usr/bin/python2.7
import socket
import StringIO

host = '159.65.90.8'
port = 31474

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot.connect((host,port))

d = bot.recv(1024)
sss = StringIO.StringIO(d)
sss.readline()
sss.readline()
sss.readline()
sss.readline()
sss.readline()
sss.readline()
data =  sss.readline()
data = data[:-4]
print data
    
print "----------------------------------"
result = str(eval(data))
print result
print "----------------------------------"

print "Sending result..."
bot.send(result + "\n")


while True:

    d = bot.recv(1024)
    sss = StringIO.StringIO(d)
    print d
    sss.readline()
    sss.readline()
    sss.readline()
    sss.readline()
    sss.readline()
    data =  sss.readline()
    print data
    data = data[:-4]
    print data
    
    print "----------------------------------"
    result = str(eval(data))
    print result
    print "----------------------------------"

    print "Sending result..."
    bot.send(result + "\n")

