from socket import *
import sys
import select
import os

host= "192.168.0.76"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf = 1024

count=0
data,addr = s.recvfrom(buf)
#how much recv -> buf
print ("file recv start from",host)

file_name = data.decode()

print("File Name : ", file_name)
data,addr = s.recvfrom(buf)
f = open(file_name, 'wb')#file create

file_size = data.decode()
print("File Size : ", file_size)

data,addr = s.recvfrom(buf)

try:
    while(data):
        count = count + len(data.decode())
        print("current_size / total_size =", count,"/",int(file_size),",",count/int(file_size)*100,"%")
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print("File Downloaded")
