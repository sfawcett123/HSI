from socket import *
import time
import json

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
for i in range(360 + 20, 260, -10):
    print( i )
    appDict = { 'heading': i }
    js = json.dumps(appDict).encode('utf-8')
    s.sendto( js , ('255.255.255.255',1234))
    time.sleep(1)
