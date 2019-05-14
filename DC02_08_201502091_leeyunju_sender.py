from socket import *
import os
import sys

s = socket(AF_INET, SOCK_DGRAM)
host = '192.168.0.76' 
port = 9999
buf = 1024
addr = (host,port)

count=0
file_name = input("Input your file : ")
n = os.path.getsize(file_name)


s.sendto(str(file_name).encode(), addr)
s.sendto(str(n).encode(), addr)

f = open(file_name, "rb")

data = f.read(buf)#read

print("File Transmit Start....")
while (data):
    count = count + s.sendto(data,addr)
    print("current_size / total_size =",count,"/",n,",",(count/n)*100,"%")
    #if(s.sendto(data,addr):#send success, return data size
    data = f.read(buf)

print("ok")
print("file_send_end")

s.close()
f.close()
