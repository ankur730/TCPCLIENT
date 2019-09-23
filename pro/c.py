#!/usr/bin/python3
from socket import *

host = "94.142.241.111"
port=23

s = socket(AF_INET, SOCK_STREAM, 0)
s.connect((host,port))

s.close()
