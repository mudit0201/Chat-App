#!/usr/bin/python
import socket
import sys
import thread
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=sys.argv[1]
port =sys.argv[2]
s.bind(("",4567))
def sending1():
	while True:
		data1=raw_input("")	
		s.sendto(data1,(ip,int(port)))
def recieving1():
	while True:
		c=s.recvfrom(100)[0]
		
		if (c!="seen"):
			s.sendto("seen",(ip,int(port)))
		print "\t\t\t\t",c
thread.start_new_thread(sending1,())
thread.start_new_thread(recieving1,())
while 1:
	pass

