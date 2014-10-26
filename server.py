#!/usr/bin/python
import socket
import thread
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.221.131"
s.bind((ip,1112))
c=s.recvfrom(100)
print c[1][0] ,int(c[1][1])
def recieving2(c):
	while True:
		print "\t\t\t\t",c[0]
		if (c[0]!="seen"):
			s.sendto("seen",(c[1][0],int(c[1][1])))	
		c=s.recvfrom(100)
def sending2():
	while True:
		data2=raw_input("")
		s.sendto(data2,(c[1][0],int(c[1][1])))

thread.start_new_thread(sending2,())
thread.start_new_thread(recieving2(c),())


while 1:
	pass
